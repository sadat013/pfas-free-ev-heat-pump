# Verification report

Date: 6 October 2026. The project is **partly reproducible**: the recovered
Python analysis runs, while the original dynamic Simscape results are not
independently reproduced. There is no experimental validation in this audit.

The owner subsequently limited MATLAB work to organizing the files for GitHub;
no further MATLAB startup or simulation is being attempted. Runtime verification
is outside the requested handoff, not a prerequisite for organizing the files.

## Executed

| Check | Outcome |
|---|---|
| Enumerate and SHA-256 hash original directory | 1,804 files; original inventory preserved locally |
| Copy selected artifacts and compare hashes | 89 copies verified byte-for-byte |
| Read final report | All 36 rendered pages, including Appendices A-D |
| Read initial proposal | All 4 pages |
| Inspect main SLX archives | Refrigerant, saved conditions, topology, key parameters and embedded functions checked without rewriting |
| Run reconstructed Appendices A-C | Successful on Python 3.12.14 |
| CoolProp calls | 102 property-cycle samples; zero fallback events |
| Python checks | 8 tests passed: speed input, power units, stopped traction, PTC heat load, exact switch boundary, no cooling, invalid mode and energy/range units |
| MATLAB static analysis | R2025a standalone `mlint.exe -id` checked the two new MATLAB functions and synthetic test; no messages after cleanup |
| CSV-to-workbook traceability | All 1,801 speed samples equal `WLTC_class_3` column E in the supplied XLS; maximum difference zero |
| Figure QA | Three generated PNGs inspected; labels, units and legends present |
| Final source preservation | All 1,804 original hashes unchanged; zero added or removed source files |
| Publication-candidate checks | 35 Git-visible files after the owner-selected MIT license was added; zero broken local Markdown links; local holds excluded; no remote configured at the time of this check |

Exact run outputs are in [verification/summary.json](verification/summary.json),
[range-sweep.csv](verification/range-sweep.csv),
[table5-comparison.csv](verification/table5-comparison.csv), and
[refrigerant-cop.csv](verification/refrigerant-cop.csv).

Test command: `python -m unittest discover -s tests -v`.
Run command: `python src/python/run_analysis.py`.

## Numerical reproduction

Source speed data produce a mean speed of 46.4989450305 km/h, maximum
131.3 km/h and mean traction demand of 5,610.33496495 W. The HVAC-off range
is 255.045488733 km. The speed plot reconstructs the reported 30-minute profile
using 1,801 samples with an elapsed axis of 0–1800 s.

Comparison to final-report Table 5 (printed p. 18):

| Ambient °C | Report R290 km | Executed R290 km | Report R1234yf km | Executed R1234yf km |
|---:|---:|---:|---:|---:|
| −25 | 172 | 171.855 | 138 | 137.536 |
| −20 | 185 | 185.105 | 145 | 144.957 |
| −15 | 197 | 196.993 | 153 | 153.224 |
| −10 | 207 | 207.719 | 189 | 201.629 |
| −5 | 217 | 217.445 | 205 | 213.864 |
| 0 | 226 | 226.305 | 218 | 224.395 |
| 5 | 234 | 234.409 | 229 | 233.554 |
| 10 | 241 | 241.850 | 238 | 241.594 |
| 15 | 248 | 248.707 | 247 | 248.707 |

The first three rows agree approximately at the reported precision, but the
R1234yf warm-side entries do not reproduce. R290 rows show inconsistent
rounding/truncation in the report. The −10 °C switch is strict: at exactly
−10 °C Appendix C uses the heat-pump branch. Its 50-point plotting grid does
not contain exactly −10 °C; the comparison above evaluates the table's exact
temperatures separately using the same functions.

Percent differences calculated from unrounded outputs are 24.952696%,
27.696845% and 28.565589% at −25, −20 and −15 °C, respectively. The report
prints 24.6%, 27.5% and 28.7%, corresponding closely to calculations from its
rounded km values. The distinction is disclosed; no source table was rewritten.

Executed Appendix B fits:

| Refrigerant | Slope (per °C) | Intercept | Fit range |
|---|---:|---:|---|
| Propane | 0.049279782714 | 2.987798245254 | −25 to 25 °C |
| R1234yf | 0.063535296956 | 2.778201784492 | −10 to 25 °C |

These are consistent with the appendix's rounded range coefficients, but not
with the separate 0.0483 R1234yf slope printed in the report prose. Original
package versions are unknown, so exact reproduction of the original fit beyond
its displayed precision is not claimed.

## Not executed or not reproduced

- MATLAB R2025a was found at the installed application path. A `-batch`
  diagnostic requesting `version`, `ver` and license availability remained at
  startup without command output for several minutes and was stopped. There
  was no successful `ver` result or license checkout confirmation. The cause
  was not conclusively diagnosed; do not describe it as a proven missing license.
- No Simscape model compiled or simulated successfully in this session.
  New MATLAB wrappers and the synthetic MATLAB test are statically reviewed
  but runtime-unverified. Their existence is not evidence of successful execution.
- MATLAB MAT objects were inspected with SciPy; standard files contain opaque
  serialized objects and several saved outputs are v7.3 HDF5 `timeseries`.
  HDF5 inspection confirms stored numeric arrays but does not establish their
  semantic signal mapping and scenario provenance. Saved-data COP was not
  reported as reproduced from those objects.
- No raw paired R1234yf output set or complete eight-case configuration set was
  recovered among the principal snapshot outputs. Dynamic temperature/COP,
  power-flow and P-h figures remain source-report artifacts.
- Solver convergence, energy balance closure, controller stability, experimental
  accuracy, uncertainty and real vehicle range remain unverified.
- Report citations were transcribed/reviewed for context, not all independently
  checked against their publications. Regulatory and safety claims were not
  adopted as current guidance.

## Report-only Simscape metrics

The following is an explicitly labeled transcription of Table 6, **not an
executed result**:

| Case | Report R290 COP | Report R1234yf COP |
|---|---:|---:|
| WLTC, −15 °C | 1.14 | 0.77 |
| WLTC, 0 °C | 0.65 | 0.67 |
| 60 km/h, −15 °C | 1.11 | 1.01 |
| 60 km/h, 0 °C | 0.67 | 0.80 |

Instantaneous and integrated COP differ. These table entries alone cannot
validate the plotted time histories or quantify experimental uncertainty.

## Reproduction boundary

Python files are **new transcriptions**, not recovered original executable
files. The report's equations/constants and supplied CSV drive the successful
run. Presentation formatting, repository layout, wrappers and tests were added
during curation. None of this verifies the broader claim of a commercially
viable or safe R290 vehicle system. Approval-required model changes are listed
in [issues](issues.md).
