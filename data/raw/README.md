# Speed input

`class3data.csv` is an unchanged copy of the source `python/class3data.csv`.
The first row is `time,speed`; the second row is the units `s,km/h`.
There are 1,801 data samples, maximum speed 131.3 km/h, and arithmetic mean speed
46.498945 km/h. The original time column resets three times at cycle-phase
boundaries, so it is not a continuous global simulation clock.

Final-report Appendix A constructs `arange(len(speed))`, giving elapsed seconds
0 through 1800. The transcription preserves this convention. Appendix C uses
the arithmetic sample mean rather than a trapezoidal time average.

All 1,801 speed values exactly match column E (data rows 8–1808) of the supplied
`WLTP-DHC-12-07e.xls`, sheet `WLTC_class_3`. That sheet labels the trace **Class 3,
version 5**, and its Explanations sheet calls it a preliminary validation cycle.
This establishes a local source match, not equivalence to a current homologation
cycle. The report attributes the input to UNECE; the exact download URL, date,
and redistribution terms still require confirmation.
Do not infer that MATLAB's `DriveCycle` object is identical to this CSV. Other
MAT files in the source contain an object named `WLTC_class_2`.
