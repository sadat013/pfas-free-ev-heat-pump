"""Traceable transcription of final-report Appendix B (printed p. 31).

Idealized steady-state property calculation and linear fits, independent of
Simscape. Temperatures entering CoolProp are K; pressure is Pa; enthalpy is
J/kg and entropy J/(kg K). COP and efficiency are dimensionless.

Inherited assumptions: condenser saturation at 50 °C, evaporator saturation
10 K below ambient, 5 K suction superheat and liquid subcooling, pressure
multipliers 0.95/1.05, and combined efficiency 0.60. A failed property call
produces COP=1 as in the report, with an added visible warning and failure list.
The fits are diagnostic outputs; they do not overwrite Appendix C coefficients.
"""
import warnings

import CoolProp.CoolProp as CP
import numpy as np
from sklearn.linear_model import LinearRegression


def calculate_cop(refrigerant: str, t_range: np.ndarray) -> tuple[np.ndarray, list]:
    """Calculate report COP samples and record any inherited fallback events."""
    cops = []
    failures = []
    t_cond_actual = 50 + 273.15
    eta_overall = 0.60
    for t_amb in t_range:
        try:
            t_evap = (t_amb - 10) + 273.15
            p_evap = CP.PropsSI("P", "T", t_evap, "Q", 1, refrigerant)
            p_suction = p_evap * 0.95
            h1 = CP.PropsSI("H", "T", t_evap + 5, "P", p_suction, refrigerant)
            s1 = CP.PropsSI("S", "T", t_evap + 5, "P", p_suction, refrigerant)
            p_cond = CP.PropsSI("P", "T", t_cond_actual, "Q", 0, refrigerant)
            p_discharge = p_cond * 1.05
            h2_ideal = CP.PropsSI("H", "S", s1, "P", p_discharge, refrigerant)
            work_actual = (h2_ideal - h1) / eta_overall
            h2 = h1 + work_actual
            h3 = CP.PropsSI("H", "T", t_cond_actual - 5, "P", p_cond, refrigerant)
            cop = (h2 - h3) / (h2 - h1)
            if cop < 1.0:
                cop = 1.0
            cops.append(cop)
        except Exception as exc:
            failures.append({"fluid": refrigerant, "temperature_c": float(t_amb),
                             "error": str(exc)})
            warnings.warn(f"Report fallback COP=1 for {refrigerant}, {t_amb} °C: {exc}")
            cops.append(1.0)
    return np.asarray(cops), failures


def fit_report_cycles() -> dict:
    """Fit propane over -25..25 °C and R1234yf over -10..25 °C inclusive."""
    temperatures = np.arange(-25, 26, 1)
    values = {}
    failures = []
    for fluid in ("Propane", "R1234yf"):
        cops, failed = calculate_cop(fluid, temperatures)
        mask = np.ones(temperatures.size, dtype=bool) if fluid == "Propane" else temperatures >= -10
        model = LinearRegression().fit(temperatures[mask].reshape(-1, 1), cops[mask])
        values[fluid] = {"cop": cops, "slope_per_c": float(model.coef_[0]),
                         "intercept": float(model.intercept_),
                         "fit": model.predict(temperatures.reshape(-1, 1))}
        failures.extend(failed)
    return {"temperature_c": temperatures, "fluids": values, "fallbacks": failures}
