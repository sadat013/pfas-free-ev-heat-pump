# Detected issues and approval-required technical changes

No equation, constant, dataset, block parameter, controller gain or algorithm in
the source archive was changed. The Python transcriptions follow the **final
appendix code**, with path handling, validation, explicit outputs, and visible
fallback warnings added. Report discrepancies are preserved as evidence.

| ID / severity | Evidence | Consequence | Proposed action and expected effect |
|---|---|---|---|
| I01 / high | Three original Python files are empty | Original executable Python workflow missing | Completed: transcribe final Appendices A-C into separately identified files; successful execution is documented |
| I02 / high | R1234yf COP slope 0.0483 in report p. 20, 0.063 in Appendix C and Figure 23 | Inconsistent stated range model | **Approval required:** establish intended coefficient and issue an explicitly versioned correction; changing it changes HVAC power and range |
| I03 / high | PTC switch −5 °C in p. 8 assumptions, −10 °C in final appendix; earlier draft also differs | Different winter performance and discontinuity location | **Approval required:** choose and justify one assumption; preserve current Appendix C transcription until then |
| I04 / high | Table 5 at −10 °C gives R1234yf 189 km; executed Appendix C gives 201.629 km | Report table cannot be fully reproduced | Completed: publish executed values with discrepancy table; **approval required** before correcting source report or changing model to fit table |
| I05 / high | Table 6 gives R290 lower COP at 0 °C (0.65 vs 0.67; 0.67 vs 0.80) | “Always higher COP” claim unsupported | Completed: qualify documentation; obtain original raw signals before diagnosing the difference |
| I06 / high | Simscape battery is 230 kg × 1,000 J/(kg K) plus fixed 1,000 W; traction Power Demand commented out | Claimed motor waste-heat/traction coupling is not demonstrated | **Approval required:** if intended, connect an evidenced speed-dependent heat source; changes thermal loads, warm-up and COP |
| I07 / high | Initial indirect-cabin safety discussion versus implemented direct cabin exchanger | Safety conclusions overreach modeled architecture | **Approval required:** design and evaluate a secondary cabin loop; changes thermal resistance, pump loads and control behavior |
| I08 / high | Different pump maxima, initial temperatures and control structure across R1234yf/R290 snapshots | Fluid comparison may be confounded by plant/control differences | **Approval required:** define matched comparisons; expected numerical direction cannot be established without simulation |
| I09 / high | `battery_T_init` referenced in R1234yf model but absent from parameter script | Clean simulation can fail or depend on stale workspace | Runner detects missing value; **approval required** to supply an intended physical initial condition |
| I10 / medium | MATLAB startup did not complete the diagnostic | Model run, licenses, toolboxes and new MATLAB wrapper unverified | Start MATLAB in a working authenticated session; run inspect and tests before simulations |
| I11 / medium | StopTime 1802 s versus report plots 1800 s | Integration boundary can change COP | **Approval required:** recover the actual report integration window; do not truncate data silently |
| I12 / medium | `.mat` copies contain WLTC_class_2; active file has opaque DriveCycle object | Class 3 identity not established for Simscape | Inspect object in MATLAB and compare time/speed to CSV; **approval required** before replacing any input |
| I13 / medium | Scenario helper references removed Variant Source and old Vehicle Speed block; sets 24 °C cabin target | Legacy helper may error or configure wrong experiment | Completed: isolate it as original reference and provide a new runner; do not invoke automatically |
| I14 / medium | Example/plot scripts assume upstream Motor Pump/Radiator/other subsystems | Incorrect execution path and stale descriptions | Completed: preserve attribution, document incompatibility and bypass those scripts |
| I15 / medium | Embedded compressor estimate divides enthalpy-flow power by 0.8; physical compressor mechanical efficiency 0.95 | “Electrical power” interpretation and possible double efficiency accounting unclear | Trace all sensors/converters; **approval required** for a boundary/efficiency correction; could materially change COP |
| I16 / medium | Report battery 39/40/42 kWh, vehicle masses 1380/1400/1730/2500 kg, motor 71/90 kW | Specifications from different scopes mixed | Completed: distinguish proposal, vehicle table, Python constants and thermal mass; **approval required** for any model harmonization |
| I17 / medium | Report says battery exchanger has 8 tubes; parameter script says 64 | Possible geometry mismatch | Inspect active block setting and intended design; **approval required** for geometry change |
| I18 / medium | General force equation includes inertia; Appendix C excludes it | Range may miss acceleration/regen behavior | **Approval required:** extend drivetrain model with specified regen and efficiency maps; no direction/magnitude guaranteed |
| I19 / medium | COP floors, fixed capacity/auxiliaries and assumed PTC transition | Performance difference depends strongly on assumptions | **Approval required:** sensitivity study or calibrated curves; report new scenarios separately |
| I20 / medium | Raw temperature/power files are MATLAB serialized objects and lack complete run metadata | Cannot prove exact scenario-to-report mapping | Preserve bytes and require MATLAB export of numeric values, units, configuration and hashes |
| I21 / publication | Team roles, coauthor agreement, third-party redistribution and dataset provenance unknown | Publication/portfolio attribution incomplete | Keep placeholders and local holds; owner confirms before release |
| I22 / low | Unit-free parameter names; unlabeled `plotse` axes; R90 legend typo | Harder to interpret output | Completed: document units and use labeled new Python figures; original snapshot scripts remain unchanged |
| I23 / low | Reference list duplicates [9]/[10] and [20]/[23]; some entries incomplete | Citation quality needs review | Preserve source report; verify and consolidate in a future report revision |

The source claims a 56.7% heating-capacity advantage by citing literature; it is
not an independently verified result of this repository. No environmental-impact
metric, measured range gain, cost saving or safety certification is inferred.

## Changes deliberately awaiting approval

Correcting the COP coefficients/switch logic, introducing inertia/regen,
normalizing controls, changing compressor efficiency accounting, changing tube
counts, and replacing the direct cabin architecture would affect results.
They remain proposals only. The expected *type* of effect is given above;
inventing a numerical benefit before running a controlled comparison would
be misleading.
