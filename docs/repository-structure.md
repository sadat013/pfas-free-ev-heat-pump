# Repository structure and copy plan

The academic source directory remains unchanged. This is a new sibling publication
candidate, not a move or rename of the original project. No pre-existing Git
repository was found at the source root or in the file inventory.

## Mapping presented before curation

Paths in the first column are relative to the original `Case Based` directory.
Every action is **copy**, except files explicitly excluded from the candidate.

| Original path | Candidate path | Treatment |
|---|---|---|
| `Copy_of_trial model/*.m`, principal `.slx`, vehicle-speed `.mat` | `models/r1234yf_snapshot/` | Exact copies; local publication hold |
| `final model r290/Copy_of_trial model/*.m`, principal `.slx`, vehicle-speed `.mat` | `models/r290_final/` | Exact copies; local publication hold |
| `tuning/Copy_of_trial model/*.m`, principal `.slx`, vehicle-speed `.mat` | `models/r290_tuning/` | Exact copies; local publication hold |
| Other `.mat` files in the latter two directories | `_private/saved-results/<variant>/` | Exact copies, no assumed scenario provenance |
| `python/class3data.csv` | `data/raw/class3data.csv` | Exact bytes; data provenance documented |
| `python/casebasedmodule.xlsx` | `_private/supporting/casebasedmodule.xlsx` | Research workbook, not an executable workflow |
| Final report, draft, proposal, presentation PDF/PPTX and temperature DOCX | `_private/reports/<original filename>` | Local reference; publication review needed |
| `report/**/*.png` | `figures/report/<original relative path>` | Original images held locally |
| `license.txt`, `readme.txt`, `drivingcycle_v2.1.8.zip` | `_private/third-party/` | Preserve driving-cycle provenance and license |
| Empty Python files | `_private/original-python/` | Preserve evidence of missing executable source |
| `matlab/` tutorials, CFD/beam examples, early `trial model/`, unpacked SLX XML, caches, backups, other ZIPs | No copy | Inventory retained; originals remain in source directory |
| Report Appendices A-C | `src/python/*.py` | Newly documented transcription; equations/constants preserved |
| No original equivalent | `src/matlab/*.m`, `tests/`, documentation | New wrappers, checks and documentation |

The exact per-file copy manifest, including SHA-256 hashes, is held at
`_private/audit/copy-manifest.csv`. The complete source inventory and archive
member inventories are also held locally, rather than disclosing all local
reference filenames and embedded metadata on GitHub.

## Proposed and implemented structure

```text
pfas-free-ev-heat-pump/
  README.md
  LICENSE
  CITATION.cff
  CHANGELOG.md
  THIRD_PARTY_NOTICES.md
  .gitignore
  requirements.txt
  requirements-audit.txt
  data/raw/class3data.csv
  docs/
    audit.md
    technical-summary.md
    workflow.md
    matlab-file-guide.md
    issues.md
    repository-structure.md
    portfolio.md
    verification.md
    verification/                 # curated executed Python evidence
  src/
    python/                      # recovered report analysis
    matlab/                      # isolated runner and COP postprocessor
  models/README.md
  models/{r1234yf_snapshot,r290_final,r290_tuning}/  # local, ignored
  figures/report/                # source figures; local, ignored
  results/README.md              # generated runs ignored
  tests/
  _private/                     # local academic sources and audit manifests
```

The owner selected MIT for original code and accompanying repository
documentation; `LICENSE` contains the standard text. Third-party exclusions
are documented in `THIRD_PARTY_NOTICES.md`. No notebooks or package scaffolding
are added because the source project contains neither.
Model snapshots remain ignored until authorship, redistribution terms, and
metadata have been reviewed. A public clone therefore supports the Python
analysis; MATLAB requires the separately supplied model snapshots.
