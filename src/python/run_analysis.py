"""Reproduce report Appendices A-C with explicit paths and new output folders.

Usage from repository root: python src/python/run_analysis.py
Optional: --cycle PATH --output NEW_DIRECTORY --skip-property-fit
Inputs are never modified. Outputs: CSV tables, JSON provenance, PNG figures.
This runs the recovered report analysis, not a Simscape simulation.
"""
import argparse
import importlib.metadata
import json
from pathlib import Path
import platform

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from range_model import calculate_ranges, get_p_motor_avg, load_cycle

ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cycle", type=Path, default=ROOT / "data/raw/class3data.csv")
    parser.add_argument("--output", type=Path, default=ROOT / "results/python-report-reproduction")
    parser.add_argument("--skip-property-fit", action="store_true")
    args = parser.parse_args()
    speeds = load_cycle(args.cycle)
    # Refuse overwrites, including valuable earlier verification outputs.
    if args.output.exists():
        parser.error("Output already exists. Choose a new --output directory.")
    args.output.mkdir(parents=True)
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False,
                         "axes.spines.right": False, "savefig.dpi": 180})

    time_s = np.arange(len(speeds))  # Appendix A: original phase-local times are not used.
    fig, ax = plt.subplots(figsize=(10, 4), layout="constrained")
    ax.plot(time_s / 60.0, speeds, color="#183c55", linewidth=1.4)
    ax.fill_between(time_s / 60.0, speeds, color="#183c55", alpha=0.08)
    ax.set(xlabel="Elapsed time (min)", ylabel="Vehicle speed (km/h)",
           title="Supplied WLTC Class 3 speed profile", xlim=(0, time_s[-1] / 60),
           ylim=(0, speeds.max() + 10))
    ax.grid(alpha=0.2)
    fig.savefig(args.output / "wltc-profile.png")
    plt.close(fig)

    temperatures = np.linspace(-25, 25, 50)  # Appendix C sampling, unchanged.
    ranges = calculate_ranges(speeds, temperatures)
    pd.DataFrame({"temperature_c": temperatures, **{f"{m}_range_km": v for m,v in ranges.items()}}).to_csv(args.output / "range-sweep.csv", index=False)
    comparison_t = np.arange(-25, 16, 5)
    comparison = calculate_ranges(speeds, comparison_t)
    comparison_table = pd.DataFrame({"temperature_c": comparison_t,
        **{f"{m}_range_km": v for m,v in comparison.items()}})
    comparison_table["propane_vs_r1234yf_percent"] = 100 * (comparison["Propane"] / comparison["R1234yf"] - 1)
    comparison_table.to_csv(args.output / "table5-comparison.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5), layout="constrained")
    styles = {"OFF": ("#888888", "--", "HVAC off"), "Propane": ("#167d6b", "-", "R290 heat pump"),
              "R1234yf": ("#386cb0", "-", "R1234yf / assumed PTC below -10 °C"),
              "PTC": ("#ba4c3b", ":", "PTC heater")}
    for mode in ("OFF", "Propane", "R1234yf", "PTC"):
        color, line, label = styles[mode]
        ax.plot(temperatures, ranges[mode], color=color, linestyle=line, label=label, linewidth=2)
    ax.set(xlabel="Ambient temperature (°C)", ylabel="Estimated range (km)",
           title="Report Appendix C: simplified driving-range estimate", xlim=(-25, 20))
    ax.grid(alpha=0.2)
    ax.legend(loc="upper left", fontsize=8)
    fig.savefig(args.output / "range-vs-temperature.png")
    plt.close(fig)

    summary = {"source": "Final report Appendices A-C, transcription",
        "python": platform.python_version(),
        "packages": {p: importlib.metadata.version(p) for p in ("numpy", "pandas", "matplotlib")},
        "cycle_samples": int(speeds.size), "elapsed_time_s": int(time_s[-1]),
        "mean_speed_kmh": float(np.mean(speeds)), "peak_speed_kmh": float(np.max(speeds)),
        "mean_traction_power_w": get_p_motor_avg(speeds),
        "hvac_off_range_km": float(ranges["OFF"][0]),
        "range_coefficients_source": "Appendix C, not automatically linked to Appendix B fit",
        "simscape_executed": False}

    if not args.skip_property_fit:
        from refrigerant_cycle import fit_report_cycles
        cycle = fit_report_cycles()
        summary["packages"].update({p: importlib.metadata.version(p) for p in ("CoolProp", "scikit-learn")})
        summary["property_fit"] = {f: {k:v for k,v in vals.items() if k in ("slope_per_c", "intercept")}
                                   for f, vals in cycle["fluids"].items()}
        summary["property_fallbacks"] = cycle["fallbacks"]
        table = {"temperature_c": cycle["temperature_c"]}
        fig, ax = plt.subplots(figsize=(9, 5), layout="constrained")
        for fluid, color in (("Propane", "#167d6b"), ("R1234yf", "#386cb0")):
            values = cycle["fluids"][fluid]
            table[f"{fluid}_cop"] = values["cop"]
            ax.scatter(cycle["temperature_c"], values["cop"], color=color, alpha=0.5, s=15)
            ax.plot(cycle["temperature_c"], values["fit"], color=color,
                    label=f"{fluid}: {values['slope_per_c']:.4f} T + {values['intercept']:.3f}")
        ax.axhline(1, color="#ba4c3b", linestyle=":", label="PTC reference")
        ax.set(xlabel="Ambient temperature (°C)", ylabel="Heating COP (-)",
               title="Report Appendix B: idealized refrigerant-cycle calculation")
        ax.grid(alpha=0.2)
        ax.legend(fontsize=9)
        fig.savefig(args.output / "refrigerant-cop-fit.png")
        plt.close(fig)
        pd.DataFrame(table).to_csv(args.output / "refrigerant-cop.csv", index=False)
    (args.output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
