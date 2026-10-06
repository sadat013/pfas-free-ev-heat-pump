# Generated runs

Run `python src/python/run_analysis.py` from the repository root. It creates
`python-report-reproduction/` and refuses to overwrite an existing directory.
Use `--output results/another-run` for a new run. All generated runs are ignored
by Git. Curated preparation-time evidence is in `docs/verification/`.

The MATLAB runner uses a new directory under `results/matlab/` for each call.
Original saved simulation files are retained in `_private/saved-results/`.
