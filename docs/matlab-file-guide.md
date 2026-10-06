# MATLAB project file guide

MATLAB preparation is limited to organization, static review and documentation.
No simulation is required for this handoff, as requested by the project owner.
Original `.m`, `.slx` and input `.mat` files are copied without numerical edits.

## Layout and variant selection

```text
models/
  r1234yf_snapshot/   # R1234yf; saved ambient -15 degC
  r290_final/         # R290; saved ambient 0 degC
  r290_tuning/        # R290; saved ambient -15 degC; additional instrumentation
src/matlab/
  run_project.m
  calculate_saved_cop.m
tests/
  test_saved_cop.m
```

These are preserved snapshots, not a controlled three-case comparison. Other
settings differ too. Folder names identify their source, not a validation status.
Do not add every folder to the MATLAB path: all three share model/helper names.
Keep each model beside its own parameter file and input data.

## Files common to all three snapshots

The common filename prefix is `ElectricVehicleThermalManagementWithHeatPump`.

| Filename after that prefix | Role and handling |
|---|---|
| `.slx` | Principal Simulink/Simscape model. Preserve its name and saved configuration. |
| `Parameters.m` | Physical parameters, component sizing and initial conditions. Inspect before any optional future run; units are given in the source comments where available. |
| `VehicleSpeed.mat` | Signal Editor input referenced by the saved model, with `DriveCycle` and `ZeroSpeed` scenarios. |
| `VehicleSpeed (1).mat`, `VehicleSpeed (2).mat` | Alternative saved input containers; not the active filename referenced by the model. Retained for provenance, not automatically substituted. |
| `Example.m` | Inherited MathWorks example narrative/helper; describes an older topology. Not the curated entry point. |
| `Scenario.m` | Legacy scenario helper referring to older block paths and settings. Do not use it to silently configure the final models. |
| `Plot1Power.m` | Legacy power plot helper referring to upstream components; can trigger simulation. Not a standalone verified plotting workflow. |

The R1234yf parameter file does not define `battery_T_init`, although the model
references it. No value has been invented. See [known issues](issues.md).

## Snapshot-specific scripts

| Location | File | Role and caution |
|---|---|---|
| `models/r290_final/` | `plotse.m` | Loads `R290_Cabin_T_60_-15.mat` and `R290_battery_T_60_-15.mat` and plots their `ans.Time`/`ans.Data`. Those saved exports are held separately under `_private/saved-results/r290_final/`, not supplied as public simulation evidence. Labels are inherited, including a typo. |
| `models/r290_tuning/` | `PlottingGraphs.m` | Calls `sim(...)` and plots `out.T_cabin_R290`. Despite the filename, it launches a simulation; do not execute it just to browse saved figures. |
| `models/r290_tuning/` | `COP_Calc.m` | Integrates `Qusefull.mat` and `P_el.mat` with `trapz`, then divides the integrals. Requires saved files and confirmed signal units/boundaries. |

Legacy scripts remain byte-preserved for traceability. Their limitations are
documented rather than silently repaired or mistaken for validated entry points.

## Added, documented helpers

- `src/matlab/run_project.m`: isolates one snapshot in a fresh output directory;
  offers inspection and optional simulation modes. Runtime remains unverified.
- `src/matlab/calculate_saved_cop.m`: preserves the original energy-ratio COP
  operation with input checks. Expected time is seconds and power is watts.
- `tests/test_saved_cop.m`: synthetic integration test for a future MATLAB
  session; not executed. It does not require running a Simscape model.

See [execution instructions](workflow.md) for optional future use. MATLAB,
Simulink, Simscape and Simscape Fluids are the principal requirements; source
headers identify R2025a Update 1. Installed toolbox availability is unverified.

## GitHub upload checklist

1. Confirm team agreement and redistribution terms for the adapted MathWorks
   models and speed inputs; review model metadata for personal information.
2. Once cleared, remove the `/models/*/` hold from `.gitignore`. It currently
   excludes the three snapshot folders, so a normal Git commit will not include
   them. Do not bypass the hold with a force-add before review.
3. Review `git status --short --untracked-files=all` and the exact selected files.
   Include approved `.m`, `.slx` and required input `.mat` files, keeping each
   variant intact. Do not upload the entire original academic directory.
4. Keep `_private/`, generated results, caches, backups and personal documents
   excluded. The root driving-cycle license is not a license for every model.
5. Confirm author/contribution placeholders and coauthor agreement. MIT has
   been selected for original project code; it does not relicense the adapted
   models or third-party inputs. Retain upstream notices.

No upload, remote, commit or model modification has been
performed. Organization is complete; publishing remains the owner's decision.
