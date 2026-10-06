# Code and execution map

## Python: independent report reconstruction

| File | Responsibility | Input | Output |
|---|---|---|---|
| `src/python/range_model.py` | Appendix C functions; CSV loading/validation | Speed km/h; ambient °C | Traction/HVAC W; estimated km |
| `src/python/refrigerant_cycle.py` | Appendix B property calls and regression | Refrigerant names; temperature grid | COP samples and linear-fit coefficients |
| `src/python/run_analysis.py` | Appendix A profile plot, C range sweep, B diagnostic fit | CSV and explicit output directory | CSV, PNG, JSON |
| `tests/test_range_model.py` | Input, dimensional and boundary checks | Supplied CSV / synthetic inputs | unittest results |

Execution order is CSV → mean traction/mean speed → HVAC demand at each
temperature → range. Property fits execute independently and are saved for
comparison. Appendix C coefficients are not automatically changed by a new
CoolProp result. No random sampling is involved.

New code changes only organization, output management, labeling and error
reporting for valid source inputs. The CLI rejects invalid speed samples and
unknown modes. It creates a fresh output directory and refuses overwrite.
Figures are rendered without an interactive GUI and were visually inspected.

The source CSV's second row contains units and is skipped; its `time` column
resets at three boundaries. The profile uses sample indices as seconds, as
Appendix A does. The range calculation preserves arithmetic sample means.
Do not “fix” the raw time column or change averaging without recording a new
experiment; even endpoint weighting can change numerical results slightly.

## MATLAB: selected snapshot, isolated work directory

1. Obtain the approved snapshot directories described in `models/README.md`.
2. Start MATLAB R2025a with required products available. From the repository
   root, `addpath('src/matlab')`.
3. Call `run_project("r290_tuning", "inspect")`. Review printed saved conditions.
4. If that configuration is intended, call
   `run_project("r290_tuning", "simulate")`.
5. Read the returned `info` and `simulationOutput`; inspect available logged
   signals before selecting outputs for a figure or COP calculation.

The runner copies one variant into a unique directory under `results/matlab/`,
loads its parameter script in a function workspace, applies those values through
`Simulink.SimulationInput`, and runs the model without rewriting saved settings.
It restores the current folder, MATLAB path and code-generation settings and
closes only the model it opened. An already loaded model of the same name causes
an error instead of being silently replaced. This wrapper has not been executed
successfully in the preparation environment.

All snapshots share the filename `ElectricVehicleThermalManagementWithHeatPump.slx`.
Renaming it casually or putting multiple variants on the path can break helper
resolution. The exact original filenames are deliberately retained.

## Recovering the report's scenario matrix

The report compares 2 refrigerants × 2 ambient conditions (−15 and 0 °C) ×
2 speed modes (WLTC and constant 60 km/h). The source does not supply eight
clearly labeled, self-contained run configurations. The folders named “final”
and “tuning” differ in more than refrigerant choice.

Before a new matched comparison, record refrigerant enumeration, ambient and
initial temperatures, speed source and data hash, cabin/battery targets, pump
and compressor limits, controller gains, solver settings, run duration,
logging configuration and useful-heat/electrical-power definitions. Save a
separate configuration for each case. Changes to those physical settings
require owner approval under this project's review policy.

The original `Scenario.m` expects a `Variant Source` and older vehicle-speed
block path. Its cold-weather target is 24 °C. The final report scenario uses
20 °C and different topology. The original `Example.m` and `Plot1Power.m`
refer to upstream branches such as Motor Pump and Radiator. They are retained
as attributed historical files, not recommended entry points.

## Saved-data COP

The supplied `COP_Calc.m` loads `Qusefull.mat` and `P_el.mat`, reads the variable
`ans` in each, integrates each signal with its own time vector, and divides
integrals. The new `calculate_saved_cop.m` preserves those operations while
validating file format, shape, finite data, interval and denominator.

Do not assume the filenames establish W, seconds, scenario or a complete
electrical boundary. Confirm those in MATLAB first. If power is in kW while
heat is W, COP is wrong by a factor of 1,000. If both use the same power units,
the ratio is unitless but the returned joule fields still require W and seconds.
No clipping, smoothing, sign correction or resampling is applied.

The synthetic MATLAB test uses known 2 kW heat and 1 kW input over 10 seconds,
for 20 kJ, 10 kJ and COP 2. It exists for a future working MATLAB session and
has not been reported as passing.
