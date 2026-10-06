# Change log

## 6 October 2026 — public GitHub publication

- Created `https://github.com/sadat013/pfas-free-ev-heat-pump` as a public repository.
- Pushed the curated `main` branch and recorded the repository URL in citation metadata.
- Replaced the portfolio-owner and GitHub-profile placeholders with Md Atiq Aziz
  and `sadat013`; individual team contribution details remain for owner confirmation.
- Private reports, source-report figures, saved results and model snapshots under
  redistribution review remain excluded by `.gitignore`.

## 6 October 2026 — MIT license selected by owner

- Created `LICENSE` with the standard MIT text and a collective project-contributor
  copyright notice for 2026.
- Added `license: MIT` to `CITATION.cff`.
- Updated `README.md`, `THIRD_PARTY_NOTICES.md`, `docs/repository-structure.md`
  and `docs/matlab-file-guide.md` to reflect the selection and third-party exclusions.
- Updated this change log. No model, scientific code, data, original report,
  third-party notice, Git publication hold, remote or commit was changed.
- Earlier verification manifests describe the preparation snapshot before
  this licensing update; no MATLAB execution was performed.

## 6 October 2026 — repository preparation

Created a separate sibling repository candidate. **Zero original files edited,
moved, renamed or deleted.** Initialized local Git on `main`; no commits,
remote, push, publication or project license were created.

### Authored files

- `README.md`: technical overview, verified Python metrics and execution instructions.
- `.gitignore`: caches, generated runs, confidential files and local publication holds.
- `CITATION.cff`: report-based team attribution, with unresolved name variant noted.
- `THIRD_PARTY_NOTICES.md`: source/license scope, provenance and conditional license recommendation.
- `requirements.txt`, `requirements-audit.txt`: tested direct runtime and optional audit dependencies.
- `data/raw/README.md`: original data units, timing and workbook match.
- `models/README.md`: snapshot placement, original helper limitations and publication status.
- `results/README.md`: output policy and non-overwrite behavior.
- `src/python/range_model.py`: documented Appendix C transcription.
- `src/python/refrigerant_cycle.py`: documented Appendix B transcription and visible fallback reporting.
- `src/python/run_analysis.py`: Appendix A plotting and reproducible CLI/export workflow.
- `src/matlab/run_project.m`: isolated as-saved snapshot runner; runtime unverified.
- `src/matlab/calculate_saved_cop.m`: validated wrapper around original trapezoidal COP equation.
- `tests/test_range_model.py`: eight non-invasive numerical/input checks, passed.
- `tests/test_saved_cop.m`: synthetic integration check, static analysis passed; not executed.
- `docs/audit.md`: classified inventory, important-file roles and audit limits.
- `docs/technical-summary.md`: report/code/interpretation distinctions and dimensional review.
- `docs/issues.md`: discrepancies, missing information and approval-required proposals.
- `docs/workflow.md`: file-level execution map and MATLAB restoration requirements.
- `docs/matlab-file-guide.md`: variant/file roles and upload checklist; MATLAB simulation explicitly outside the owner-requested organization scope.
- `docs/repository-structure.md`: pre-copy mapping and implemented layout.
- `docs/portfolio.md`: summary, project achievements, CV and LinkedIn drafts with contribution placeholders.
- `docs/verification.md`: executed and unverified checks, report comparisons and limitations.
- `docs/verification/input-traceability.json`: exact CSV-to-XLS speed comparison.
- `CHANGELOG.md`: this record.

### Copied files and generated evidence

89 source artifacts were copied byte-for-byte: selected SLX/parameter/helper/input
snapshots, saved results, source reports/presentation, report PNGs, original empty
Python files, the speed CSV, research workbook and driving-cycle provenance.
The exact original-to-new path for **every copy** is recorded in
`_private/audit/copy-manifest.csv`, with SHA-256 verification. Original copied
MATLAB files were not reformatted or scientifically changed; new documentation
and entry points sit alongside the snapshots.

Generated Python files copied to `docs/verification/`:

- `summary.json`
- `range-sweep.csv`
- `table5-comparison.csv`
- `refrigerant-cop.csv`
- `wltc-profile.png`
- `range-vs-temperature.png`
- `refrigerant-cop-fit.png`

The corresponding run outputs are preserved in the ignored
`results/python-report-reproduction/` directory. Private audit evidence includes
`inventory.csv`, `archives.json`, `models.json`, `model-evidence.json` and
`mat-containers.json`. Final checks add `repository-checks.json`,
`change-manifest.csv`, and an environment package listing under `_private/audit/`.
`change-manifest.csv` enumerates every non-Git, non-cache file in the final
candidate with its creation/copy classification and inclusion status.

### Local inspection workspace

Outside this repository, a private `.case-based-audit` working directory was
created in the active Codex workspace. It contains the inspection scripts
`render_report.py`, `inspect_sources.py`, `inspect_data.py`,
`inspect_workbook_images.py`, `curate.ps1`, and `verify_repository.py`, report
page renders, workbook image contact sheets, extracted text/JSON inventories,
and an isolated Python environment. These are preparation artifacts, not changes
to the academic source and not part of the GitHub candidate.

### Scientific changes not applied

No constants, equations, datasets, control gains, Simscape blocks or assumptions
were silently corrected. Conflicting report values and potential model changes
are documented in `docs/issues.md`. No simulated vehicle results were presented
as measurements; no MATLAB runtime success was claimed.
