# Project audit

Audit date: 6 October 2026. Primary context: the complete final report dated
5 February 2026. All 36 PDF pages were rendered and read, including equations,
figures, tables, references and code appendices. The four-page initial proposal
was read completely. The presentation PDF was extracted across all 33 slides;
its PPTX text and the temperature DOCX were inspected. The draft report was
examined as an earlier version, not substituted for the final.

## Inventory

The source contains **1,804 files**, totaling **229,089,165 bytes** (218.48 MiB).
SHA-256 grouping found **255 duplicate-content groups**, with **891 additional
copies** beyond one representative per group. Duplicate content does not prove
which version is authoritative; distinct model variants remain distinct.

The complete per-file inventory is `_private/audit/inventory.csv` (relative path,
bytes, hash, category). ZIP/MLPROJ member lists are in
`_private/audit/archives.json`; 17 archive containers, including autosave and
project containers, were examined. No `.py`, `.csv`, `.tex` or `.bib` members
were found in those archive member lists. No native `.ipynb` notebook, Python
package, requirements file, or report LaTeX source was found.

| Classification | Files | Disposition |
|---|---:|---|
| Generated files or backups | 1,020 | Excluded from candidate |
| Reference/tutorial material | 393 | Retained at original location |
| Unpacked Simulink internals | 235 | Excluded; preserved in source |
| Report figures/draft text | 39 | Relevant PNGs copied locally |
| Third-party driving-cycle material | 35 | License and ZIP retained locally |
| MATLAB source code in project variants | 23 | Principal variants copied; historical baseline inventoried |
| MATLAB inputs/results in project variants | 23 | Principal inputs and saved results copied locally |
| Other archives | 11 | Indexed; original files preserved |
| Supporting/unclear | 8 | Retained in source |
| Reports/proposal/presentation | 6 | Copied to local private reference folder |
| Python source/data and root spreadsheet | 6 | Empty scripts preserved; CSV used; spreadsheets inspected |
| Principal/historical EV Simulink models | 5 | Three selected; two earlier baselines retained at source |

These are mutually exclusive audit categories, not extension counts. Across
all files there are 171 `.m`, 45 `.slx`, 232 `.mat`, one `.mlx`, and three `.py`
files. Most MATLAB files outside the project variants belong to a refrigeration
tutorial and CFD/beam demonstrations, not the final report's execution chain.

## Important files and their roles

| Original file/group | Role and evidence |
|---|---|
| `DENSYS_Case_Base_Module_2025_26 FINAL1.pdf` | Primary final report; 36 image-only pages; includes executable logic as screenshots in Appendices A-C |
| `Case Based PFAS.pdf` | Initial assignment; A-segment BEV, 2,500 kg gross mass, 40 kWh battery, 90 kW motor; these differ from the final vehicle specification |
| `DENSYS_Case_Base_Module_2025_26 DRAFT single.pdf` | Earlier 25-page report; contains editorial notes and different Python coefficients/switch temperature |
| `Copy of Automotive Technology Consulting.pdf/.pptx` | 33-slide presentation; uses the same COP comparison table; individual responsibility is not established |
| `Cabin&Battery Tempereature Graphs.docx` | Supporting temperature-plot document; not the primary result source |
| `report/` | Schematics, control diagrams, temperature/COP plots, P-h diagrams and power-flow plots used in the report |
| `report/reference for 60kmph writing.txt` | Draft narrative with embedded LaTeX fragments; internally refers to WLTC, despite filename |
| `python/class3data.csv` | Speed input used by the report Appendix A/C transcriptions |
| `python/compressorfinal.py`, `ptcexplaned.py`, `ptcinfluence.py` | All zero bytes; cannot be treated as runnable original code |
| `python/casebasedmodule.xlsx` | Research workbook: five sheets with little cell data, plus 22 embedded images inspected visually; these include vehicle specifications, range/consumption screenshots, a vehicle photograph and decorative arrows |
| `WLTP-DHC-12-07e.xls` | Local source of the CSV speed trace: all 1,801 speeds exactly match column E of `WLTC_class_3`; sheet labels it Class 3 version 5 and explanations call it a preliminary validation cycle |
| `Copy_of_trial model/...slx` | R1234yf snapshot, confirmed by the refrigerant property enumeration |
| `final model r290/Copy_of_trial model/...slx` | Propane snapshot, saved at 0 °C ambient |
| `tuning/Copy_of_trial model/...slx` | Propane snapshot at −15 °C with added power/heat instrumentation and MATLAB Function blocks |
| `*Parameters.m` | Scalar geometry, initial state, pump and compressor values; scripts differ among snapshots |
| `*Example.m` | Identical MathWorks example walkthrough in five locations; references removed/renamed upstream subsystems |
| `*Scenario.m` | Legacy mutator for an upstream topology; cold-weather cabin target 24 °C conflicts with the current 20 °C scenario constants |
| `*Plot1Power.m` | Legacy power extraction requiring Motor_Pump and Radiator branches; can launch a simulation implicitly |
| `tuning/.../COP_Calc.m` | Ratio of trapezoidal integrals of saved `ans` timeseries; lacks validation and documented units |
| `tuning/.../PlottingGraphs.m` | Runs the model then plots `out.T_cabin_R290`; not a complete case sweep |
| `final model r290/.../plotse.m` | Loads two R290 MAT files and plots cabin/battery temperatures; axis labels/units absent and legend has R90 typo |
| `*VehicleSpeed.mat` | Opaque MATLAB objects named DriveCycle and ZeroSpeed; active Signal Editor file in all three main snapshots |
| `*VehicleSpeed (1).mat`, `(2).mat` | Objects named WLTC_class_2; do not relabel as Class 3 |
| `R290_1560.mat`, temperature MATs, `P_el.mat`, `Qusefull.mat` | Saved outputs; MATLAB object serialization prevents full semantic recovery with a basic SciPy reader |
| `trial model/`, `matlab/files/` | Earlier EV template variants; retained as historical context, not selected as final |
| `drivingcycle*`, root installer/readme/license | Daniel Auger/Cranfield driving-cycle package; separate license scope |
| `matlab/Models`, `Scripts`, `CFD_Objects`, `Docs` | Tutorial/reference material; not the report's final model chain |
| Root `simulink/`, `metadata/`, `_rels/`, `[Content_Types].xml` | Expanded model-container content, not a standalone additional source model |

`ElectricVehicleThermalManagementWithHeatPump.slx.zip` is byte-identical to the
tuning `.slx`; its extension does not make it an independent model. The source
also contains 360 HTML files, primarily generated help/reports, not publication
documentation written for this project.

## Publication risks

The largest source artifact is the 62,806,049-byte presentation. Two tutorial
ZIPs are approximately 46 MB and 22 MB. None of the source files exceeds 100 MiB,
but these assets add substantial repository weight and are not needed for the
curated workflow. Drafts contain unfinished editorial text. Reports/proposal
include third-party figures, institutional branding and supervisor contact
details. SLX/MAT metadata may embed author/machine information. Those materials
are held locally rather than automatically included in a public Git history.

No project-wide license or root Git repository existed. The nested tutorial has
its own README, security guidance and ignore/attributes files; these do not
define the new repository's scope or license. No source file was removed,
renamed, rewritten or moved during curation. 89 selected source artifacts were
copied and checked against their SHA-256 hashes.

## Audit limits

All source files were enumerated and hashed; archives were indexed. Deep
engineering review focused on the final report, proposal, actual EV variants,
their scripts, data containers and supporting plots. Unrelated CFD/beam code
and generated cache internals were classified, not validated as independent
engineering projects. MATLAB object values, model compilation and complete
toolbox requirements remain unverified. The restrictions and approvals needed
for public release cannot be inferred from directory possession alone.
