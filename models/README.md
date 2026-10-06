# Academic Simscape snapshots

See the [MATLAB file guide](../docs/matlab-file-guide.md) for each script's role,
variant layout and GitHub upload checklist. No MATLAB simulation is required
for this organization task.

Three byte-preserved local snapshots are supplied with this working folder:
`r1234yf_snapshot`, `r290_final`, and `r290_tuning`. Their original filenames
are retained because model names and helper functions depend on them. Never
add all three folders recursively to the MATLAB path: they contain identical
model/function names with different contents.

The directories are ignored by Git pending redistribution, team authorship,
and embedded metadata review. They are not downloaded automatically. A public
clone must obtain the approved snapshots from the project owner and place
them here before running MATLAB. See [workflow](../docs/workflow.md) and
[copy mapping](../docs/repository-structure.md).

The `*Example.m`, `*Scenario.m` and `*Plot1Power.m` files are inherited from a
MathWorks example and describe an older topology. Preserve their notices;
do not use them as the curated project's entry point. The supplied runner
copies one selected snapshot to a fresh results directory and runs only its
parameter script and model. MATLAB execution is currently unverified.
