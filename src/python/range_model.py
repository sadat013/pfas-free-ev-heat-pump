"""Final-report Appendix C range model, transcribed and documented in October 2026.

Source: February 5, 2026 final report, printed pp. 32-33 (PDF pp. 33-34).
The original three .py files were empty. This is a traceable reconstruction,
not recovered executable source. All numerical constants and operations in
the range calculation follow Appendix C, including its simplifying assumptions.

Input: speed samples in km/h at uniform one-second intervals.
Outputs: mean traction demand [W], HVAC demand [W], estimated range [km].
No acceleration, regenerative braking, battery-temperature derating, cooling,
or dynamic Simscape outputs enter this calculation.
Dependencies: NumPy; the CSV reader uses pandas.
Run through run_analysis.py; importing this module performs no simulation.
"""
from pathlib import Path

import numpy as np
import pandas as pd

BATTERY_CAP_KWH = 39.0
BASE_ELECTRONICS_W = 1500.0
MODES = ("OFF", "PTC", "R1234yf", "Propane")


def load_cycle(path: Path) -> np.ndarray:
    """Load the supplied CSV's speed column, skipping its second, units row.

    Its original time column resets at phase boundaries. Appendix A constructs
    elapsed time using sample indices; preserve that convention in this project.
    """
    frame = pd.read_csv(path, skiprows=[1])
    if "speed" not in frame:
        raise ValueError("Input CSV requires a speed column in km/h.")
    speeds = frame["speed"].to_numpy(dtype=float)
    if speeds.size < 2 or not np.all(np.isfinite(speeds)) or np.any(speeds < 0):
        raise ValueError("Speed samples must be finite, nonnegative and nonempty.")
    return speeds


def get_p_motor_avg(speed_array: np.ndarray) -> float:
    """Mean rolling-plus-aerodynamic traction power [W], Appendix C.

    Uses m=1400 kg, g=9.81 m/s², Crr=0.012, rho=1.225 kg/m³,
    A=2.4 m², Cd=0.3 and drivetrain efficiency=0.9. Stops consume zero
    traction power; auxiliary power is added separately. Sample averaging is
    deliberately preserved instead of replacing it with numerical integration.
    """
    m, g, crr, rho, area, cd, eta = 1400.0, 9.81, 0.012, 1.225, 2.4, 0.3, 0.9
    powers = []
    for v_kmh in speed_array:
        if v_kmh <= 0:
            powers.append(0.0)
            continue
        v_ms = v_kmh / 3.6
        power = ((m * g * crr + 0.5 * rho * area * cd * v_ms**2) * v_ms) / eta
        powers.append(power)
    return float(np.mean(powers))


def get_hvac_power(mode: str, t_amb: float) -> float:
    """HVAC electrical power [W] at ambient temperature [°C].

    Cabin target 20 °C; heat-loss coefficient 135 W/K. R1234yf switches to
    PTC strictly below -10 °C. COP slopes are 0.049 and 0.063 per °C;
    the 1.1 floor is an inherited modeling assumption, not a physical law.
    """
    t_target = 20.0
    h_loss = 135.0
    q_required = max(0, h_loss * (t_target - t_amb))
    if mode == "OFF":
        return 0.0
    if mode == "PTC":
        return q_required
    if mode == "Propane":
        cop = 0.049 * t_amb + 2.99
        return q_required / max(1.1, cop)
    if mode == "R1234yf":
        if t_amb < -10:
            return q_required
        cop = 0.063 * t_amb + 2.78
        return q_required / max(1.1, cop)
    raise ValueError(f"Unknown HVAC mode: {mode!r}")


def calculate_ranges(speeds_kmh: np.ndarray, temperatures_c: np.ndarray) -> dict:
    """Return one range array [km] per HVAC mode; no state is modified."""
    p_motor_avg = get_p_motor_avg(speeds_kmh)
    v_avg_kmh = float(np.mean(speeds_kmh))
    ranges = {mode: [] for mode in MODES}
    for temperature in temperatures_c:
        for mode in ranges:
            p_hvac = get_hvac_power(mode, float(temperature))
            total_p_kw = (p_motor_avg + BASE_ELECTRONICS_W + p_hvac) / 1000.0
            hours_of_drive = BATTERY_CAP_KWH / total_p_kw
            ranges[mode].append(hours_of_drive * v_avg_kmh)
    return {mode: np.asarray(values) for mode, values in ranges.items()}
