# Engineering interpretation and source traceability

References below use **printed report page numbers**; add one for PDF page
numbers because the cover is unnumbered. The final report is the primary source.
Labels distinguish **Report**, **Code**, **Executed**, and **Interpretation**.

## Objective and boundaries

**Report:** compare R290 and R1234yf for winter heating of an A-segment EV's
cabin and battery. The final reference vehicle is the Hyundai Inster Standard
Range with 39 kWh usable energy and 42 kWh nominal energy (Table 3, p. 5).
The proposal instead specifies 40 kWh, 2,500 kg gross mass and a 90 kW motor.
The report's vehicle table lists 1,380 kg unladen, 1,730 kg gross and 71 kW;
Appendix C actually calculates with 1,400 kg. Those values are not interchangeable.

**Code:** two distinct numerical methods exist. Python is a steady-state
energy/range estimate. Simscape is a transient thermal-fluid/control model.
There is no verified file interface coupling the Python calculation to Simscape,
and neither is an experimentally calibrated vehicle-range predictor.

## Vapor-compression model

**Report, pp. 6 and 10-14:** compressor, heat rejection to cabin/battery branches,
throttling valve, ambient heat absorption, and return to the compressor. The
ideal cycle description uses isentropic compression, isobaric heat exchange,
and isenthalpic throttling. Real modeled compressor efficiencies and pressure
losses mean the ideal-cycle description is not a full solver specification.

For negligible kinetic and potential energy, a steady component balance is
$\dot Q-\dot W=\dot m(h_\mathrm{out}-h_\mathrm{in})$, with work positive out
of the control volume. Compressor input is instead written positive into it:
$\dot W_\mathrm{comp,in}=\dot m(h_2-h_1)$. State that convention when comparing
the two equations. A cycle-only heating COP is
$(h_2-h_3)/(h_2-h_1)$; it omits auxiliary loads and heat-delivery losses unless
those are deliberately included in its boundary.

**Appendix B transcription, executed:** CoolProp saturation conditions are
50 °C at the condenser and ambient minus 10 K at the evaporator. Suction
superheat and liquid subcooling are 5 K. Suction/discharge pressures are
multiplied by 0.95/1.05. Actual compression enthalpy rise is ideal rise divided
by a combined efficiency of 0.60. COP values below one and property-call
failures are replaced with one in the original algorithm. The reconstruction
preserves this but warns and records fallback events; none occurred in the run.

Propane is fitted over −25 through 25 °C; R1234yf is fitted only over −10 through
25 °C. Plotting its line below −10 °C is **extrapolation**, not a fitted cold-range
model. Fit results were 0.049280 per °C and intercept 2.987798 for propane,
and 0.063535 per °C and intercept 2.778202 for R1234yf. The range code deliberately
retains its printed rounded coefficients rather than silently replacing them.

## Simplified range analysis

**Appendix C:** rolling resistance and aerodynamic drag generate per-sample
traction power. Although the report introduces $m a$ in the general tractive
force equation, its appendix code omits acceleration and regenerative braking.
It averages power over equally weighted speed samples. It does not calculate
drag at mean speed; the speed-cubed term is evaluated at each sample first.

| Parameter | Value used by Appendix C | Units |
|---|---:|---|
| Vehicle mass | 1,400 | kg |
| Gravity | 9.81 | m/s² |
| Rolling coefficient | 0.012 | dimensionless |
| Air density | 1.225 | kg/m³ |
| Frontal area | 2.4 | m² |
| Drag coefficient | 0.3 | dimensionless |
| Drivetrain efficiency | 0.9 | dimensionless |
| Usable energy | 39 | kWh |
| Constant auxiliary load | 1,500 | W |
| Cabin heat-loss coefficient | 135 | W/K |
| Cabin target | 20 | °C |

Cabin demand is $\max(0,135(20-T_\mathrm{amb}))$ W. PTC draws that power directly.
Propane uses $\max(1.1,0.049T_\mathrm{amb}+2.99)$ as COP. R1234yf uses PTC below
−10 °C, otherwise $\max(1.1,0.063T_\mathrm{amb}+2.78)$. The floor and switch are
assumptions; they are not universal refrigerant operating limits.

Total power combines average traction, auxiliaries and HVAC. Battery energy in
kWh divided by power in kW gives operating hours, multiplied by mean speed in
km/h to give km. At temperatures above 20 °C the model assumes zero HVAC heat
demand; it does not include air conditioning. Available battery capacity is
constant with temperature, state of charge, discharge rate and age.

**Executed:** 1,801 speed samples, 1800 s index time, 46.498945 km/h arithmetic
mean, 131.3 km/h maximum, 5,610.334965 W mean traction power. Range results and
Table 5 discrepancies are in [verification](verification.md).

## Transient Simscape architecture and controls

**Report, pp. 10-15; confirmed structurally in the model:** a two-phase refrigerant
loop heats moist cabin air directly through an inner condenser and heats a
secondary battery coolant through a refrigerant-liquid exchanger. Controlled
orifices split refrigerant flow. A compressor, expansion device, ambient
heat exchanger, cabin blower and battery coolant pump complete the main plant.

**Code:** fluid property blocks select R1234yf or Propane. Thermal-liquid
properties select ethylene glycol; mixture concentration has not been verified.
The battery is a thermal mass, 230 kg with specific heat 1,000 J/(kg K), plus
a constant 1,000 W heat source. Its thermal capacitance is therefore
230,000 J/K. This is not an electrochemical 40 kWh storage model. The speed-based
`Power Demand` subsystem and its motor/battery-demand outputs are commented
out. Speed is still connected to `v_vehicle` through Signal Editor and can
affect air-side conditions, but that does not establish a dynamic traction heat
load in the battery source.

The cabin equation $C_\mathrm{cab}\,dT/dt=\dot Q_\mathrm{cab}-\dot Q_\mathrm{loss}$
is a lumped explanatory balance. The source cabin implementation includes moist
air and occupancy-related gains rather than merely the Python 135 W/K formula.
Battery balance is $C_\mathrm{bat}\,dT/dt=\dot Q_\mathrm{cool,bat}+\dot Q_\mathrm{gen}$.
Coolant sensible heat follows $\dot m c_p(T_\mathrm{out}-T_\mathrm{in})$;
reverse the sign when describing heat removed from the coolant into the battery.

**Report control intent:** cabin and battery temperature errors drive compressor
PI control; pressure cutoffs protect operation; expansion control uses superheat
(7 K reference visible in model); two valve controllers prioritize cabin demand;
blower and pump controls regulate cabin and battery heat delivery. Gains,
saturations, and disabled blocks differ across model snapshots. This preparation
does not claim controller optimization, formal stability analysis or calibrated
performance.

| Setting | R1234yf snapshot | R290 final | R290 tuning |
|---|---:|---:|---:|
| Saved ambient (°C) | −15 | 0 | −15 |
| Cabin / battery target (°C) | 20 / 20 | 20 / 20 | 20 / 20 |
| Nominal simulation stop (s) | 1802 | 1802 | 1802 |
| Pump speed maximum in script (rpm) | 1,000 | 6,000 | 6,000 |
| Battery initial value in script | **missing** | 0 °C | −15 °C |
| Compressor displacement | 80 cm³/rev | 80 cm³/rev | 80 cm³/rev |
| Compressor speed maximum | 3,600 rpm | 3,600 rpm | 3,600 rpm |
| Compressor mechanical efficiency | 0.95 | 0.95 | 0.95 |

The constant-speed block contains 60 km/h, but merely finding that block does
not establish it is the active input. The saved scenario uses Signal Editor
`DriveCycle`. Its object needs MATLAB to verify the actual speed trajectory.

## Dimensional consistency and ambiguous quantities

- $mgC_\mathrm{rr}$ and $\rho A v^2/2$ have units N; multiplying by m/s gives W.
- A difference of two °C temperatures has the same magnitude as a K difference;
  thermodynamic property calls and absolute-temperature ratios require K.
- CoolProp `PropsSI` returns J/kg and Pa; Simscape converters may output kJ/kg
  and MPa. The tuning compressor function explicitly multiplies by 1,000 and
  divides by 0.8. Confirm converter units and the meaning of 0.8 before treating
  that result as electrical power or changing it.
- The tuning coolant functions also multiply specific heat by 1,000. The blower
  enthalpy function has no such factor. These different fluid-domain outputs
  need their converter settings checked; a missing factor cannot be inferred
  solely from the code's appearance.
- `coolant_tank_volume=1.25` is liters in the model block, not m³.
  `pump_displacement=0.02` is liters/revolution. Compressor displacement is cm³/rev.
- The scalar `hex_N_tubes=64` conflicts with the report's description of 8 tubes.
  Determine active block parameterization before changing either statement.
- The report calls integrated COP an average. Ratio-of-integrals and
  mean-of-ratios generally differ. Useful-heat sign, electrical/shaft-power
  boundary, auxiliary inclusion and averaging interval require explicit records.

## Results and conclusions: what is supported

**Report Table 6, p. 25:** R290/R1234yf COPs are 1.14/0.77 for WLTC at −15 °C;
0.65/0.67 for WLTC at 0 °C; 1.11/1.01 for 60 km/h at −15 °C; and 0.67/0.80
for 60 km/h at 0 °C. These are transcribed report values, not reproduced outputs.
They do not support a claim that R290 has higher integrated COP in every case.

**Report Figures 25-28:** R290 provides warmer cabin conditions at −15 °C,
with similar battery warming in the compared traces. The prose's assertion of
maintaining the cabin target should be qualified because plotted temperatures
fall later in several cases. No raw paired R1234yf result set was found among
the selected top-level outputs.

**Interpretation:** the study is a useful comparative thermal-systems modeling
exercise and shows why both useful heat and power must be assessed over a
specified boundary and interval. It does not demonstrate a drop-in commercial
replacement, a quantified lifecycle benefit, or a validated driving-range gain.
Safety architecture, full scenario provenance, physical validation, economic
analysis and sensitivity/uncertainty evaluation remain open work.
