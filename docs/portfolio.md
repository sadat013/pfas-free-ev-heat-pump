# Portfolio presentation draft

## Short title

Winter EV Heat-Pump Modeling

## One-line description

Comparing R290 and R1234yf for EV cabin and battery heating through thermodynamic analysis, Python range estimation, and Simscape modeling.

## Project summary

This DENSYS master's team project examined how refrigerant selection affects
winter thermal management in a compact battery electric vehicle. The study
combined an idealized refrigerant-cycle calculation and WLTC-based Python range
estimate with a separate Simscape model of cabin and battery heating. Propane
(R290) was compared with R1234yf under cold-weather conditions, with attention
to thermal performance, control behavior, and implementation constraints.
Repository preparation recovered the Python workflow from the final report,
documented model assumptions, and identified discrepancies between reported
tables and executable equations. The reconstructed range analysis executes
successfully; the dynamic Simscape results remain unverified by rerunning.
The project demonstrates a structured approach to energy-system modeling and
technical traceability, while making the limits of simplified simulations and
propane safety assumptions explicit.

## Engineering challenge

Evaluate how heating demand competes with propulsion for limited battery energy,
and whether refrigerant performance remains favorable once thermal delivery,
controls and system boundaries are considered. Keep idealized range estimates
separate from transient heat-pump simulations.

## Personal technical contribution — confirm before use

Portfolio owner: **Md Atiq Aziz**. The report/presentation author spelling differs;
confirm the preferred formal citation spelling before changing report attribution.
Role: **[confirm personal tasks in refrigerant selection, Python modeling,
Simscape plant development, controller design, analysis and report writing]**.
Team responsibilities: **[confirm allocation]**.

Do not present the full team model or the repository curation as solely your
original work. Replace the placeholders before using first-person wording.

## Tools and methods

MATLAB R2025a, Simulink, Simscape Fluids, Python, NumPy, pandas, Matplotlib,
CoolProp and scikit-learn; vapor-compression cycles, energy balances,
WLTC speed inputs, lumped thermal modeling, PI feedback control, linear
regression, performance comparison and reproducibility checks.

## Achievement statements — project-level, not yet personal claims

- Compared two refrigerants using distinct thermodynamic, range and transient
  thermal-model perspectives, documenting the boundary of each method.
- Modeled a hybrid direct-cabin/indirect-battery heating architecture and examined
  compressor, valve, blower and coolant-pump control behavior in the team study.
- Reconstructed and executed the report's Python workflow using 1,801 speed
  samples, with explicit inputs, versioned dependencies and saved result tables.
- Identified reproducibility issues involving COP assumptions, scenario settings,
  reported ranges and the distinction between integrated and instantaneous COP.

The last two bullets describe repository-preparation work. Attribute them as
such unless you independently performed that work and can explain it.

## Verified metrics suitable for a portfolio

The executed simplified analysis estimates **196.99 km for R290 versus
153.22 km for the assumed R1234yf/PTC case at −15 °C**, a **28.57% modeled
difference** under the report appendix's assumptions. The R1234yf branch is
forced to resistive heating below −10 °C. This is **not a measured range gain**
and not a direct comparison of experimentally validated heat-pump hardware.

The report's dynamic COP values of 1.14 versus 0.77 at −15 °C may be discussed
only as *report-sourced simulation results not rerun in repository verification*.
Do not state that R290 won every case: Table 6 has lower R290 COPs at 0 °C.

## Skills demonstrated by the project

Thermodynamics; EV thermal management; system boundaries; refrigerant-property
analysis; MATLAB/Simulink modeling; Python scientific computing; control logic;
dimensional checks; engineering visualization; technical writing; reproducibility
and source attribution. Select only the skills supported by your own contribution.

## Learning reflection — adapt to your experience

“[Confirm before using:] I learned to distinguish idealized cycle efficiency
from heat delivered by a controlled system, and to trace performance claims
back to equations, inputs and operating conditions. I also learned why a
thermodynamic comparison alone cannot establish refrigerant safety or a
vehicle's real-world range.”

## Suggested visuals

1. Use the regenerated [range-versus-temperature figure](verification/range-vs-temperature.png)
   with its PTC-switch assumption and simulated-result caption visible.
2. Add the [refrigerant COP plot](verification/refrigerant-cop-fit.png), explaining
   the different regression ranges and the lack of automatic coupling to Simscape.
3. After permission review, use the original architecture diagram and one cabin/
   battery temperature comparison, with team attribution and “report result,
   not independently rerun” in the caption.
4. Show the README workflow diagram to distinguish the two modeling approaches.

## Suggested GitHub topics

`energy-systems`, `electric-vehicles`, `thermal-management`, `heat-pump`,
`refrigerants`, `matlab`, `simulink`, `simscape`, `python`, `coolprop`,
`thermodynamics`, `wltc`, `reproducible-research`.

## CV bullet — contribution placeholder required

Contributed **[specific responsibility]** to a DENSYS team study comparing R290
and R1234yf EV heat pumps using Python and MATLAB/Simscape, analyzing winter
heating performance and documenting model assumptions and reproducibility limits.

## LinkedIn project description

DENSYS master's team project investigating R290 as a non-fluorinated refrigerant
candidate for winter EV thermal management. Combined thermodynamic property
analysis, a WLTC-based Python range estimate and Simscape cabin/battery heating
models. My contribution: **[confirm specific responsibilities]**. The repository
documents inputs, assumptions, execution instructions and verification limits;
modeled range estimates are distinguished from experimentally validated results.

## Public contact placeholders

Name: Md Atiq Aziz · GitHub: [sadat013](https://github.com/sadat013) · Portfolio: [add URL] ·
Contact: via GitHub profile. Avoid using other team members' or the
supervisor's email addresses as your project contact.
