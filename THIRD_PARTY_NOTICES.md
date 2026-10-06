# Attribution and license scope

The project owner selected the [MIT License](LICENSE) on 6 October 2026 for
original project code and accompanying repository documentation. Existing
third-party notices and terms remain in force. The MIT grant does not cover
rights owned by third parties or resolve outstanding coauthor permissions.

## Original academic study

The final report credits A. Aziz, A. E. Güngör, A. Hodžić and
V. Van Scyoc Hernandez, supervised by Chrisle Joseph Charls. Python
implementations in this candidate transcribe the final report's Appendices A-C;
they are not claimed as a new thermodynamic model. Obtain the team's publication
agreement and confirm the portfolio owner's individual contribution.

The proposal and reports contain names, supervisor contact details, university
branding, and third-party figures. Local copies remain in `_private/` and are
excluded by `.gitignore`. No institution restriction was conclusively established
from the reviewed material; publication permission remains unknown.

## MathWorks source models

Original helpers carry `Copyright 2024 The MathWorks, Inc.` and the tutorial
folder carries a 2022 MathWorks notice. The report identifies the MathWorks
thermal-management template as its starting point. The matching official example
is [Electric Vehicle Thermal Management with Heat Pump](https://www.mathworks.com/help/hydro/ug/ElectricVehicleThermalManagementWithHeatPump.html).

Copyright notices are retained in copied files. The source root's `license.txt`
does **not** establish licensing for all MATLAB content: it explicitly credits
Cranfield University and accompanies the driving-cycle package. Do not apply
that license to the MathWorks examples or the team's report. Confirm the terms
governing redistribution of the adapted models before removing their Git ignore
rule. An attribution link alone is not a redistribution grant.

## Driving-cycle library

The bundled *Driving Cycle (Simulink Block)* identifies Daniel Auger as its author.
Its `license.txt` contains a three-condition BSD-style notice, copyright
2013–2024 Cranfield University. Copies of that notice, its readme, and the
original ZIP are retained locally in `_private/third-party/`. This library is
not required by the recovered Python workflow; the selected model snapshots
reference a Signal Editor MAT file. The library's presence does not prove it
generated the exact report runs.

## Speed data

The report attributes `class3data.csv` to UNECE. Its 1,801 speed values exactly
match the supplied `WLTP-DHC-12-07e.xls`, sheet `WLTC_class_3`, labeled Class 3
version 5; the workbook describes a preliminary validation cycle. The supplied
files do not record an exact download URL, retrieval date or standalone dataset
license. Preserve that uncertainty; do not invent a citation. The CSV is kept
byte-for-byte and its hash is recorded in the local copy manifest. Confirm
external provenance before public release. Original phase-local timestamps are
not rewritten.

## MIT scope and exclusions

The root `LICENSE` uses the standard [MIT license text](https://opensource.org/license/mit).
Its copyright notice identifies the project contributors collectively rather
than asserting that one portfolio owner holds all team rights.

The grant applies to original project code in `src/`, the added tests, and
accompanying authored repository documentation, to the extent the contributors
hold the necessary rights. It excludes copied MathWorks material and adapted
model snapshots in `models/`, the driving-cycle package, externally sourced
data in `data/raw/`, source-report figures in `figures/report/`, and source
reports and other material held in `_private/`. Retain their existing notices;
do not infer permission to redistribute them from the root MIT license.

Confirm coauthor agreement before public release. Selecting MIT does not
publish this repository or remove the existing model/report publication holds.
