# Reproducibility Protocol

## Principle

All experiments should be runnable from a clean environment with deterministic seeds and explicit outputs.

## Environment Setup

1. Create virtual environment.
2. Install exact dependencies from `requirements.txt`.
3. Run a single RQ script and verify output file creation under `results/`.

## Determinism

- Set fixed RNG seeds in experiment scripts.
- Record all command-line parameters.
- Keep input topology immutable during the run.

## Logging

For each run, capture:
- timestamp
- git commit hash
- script name
- seed and iteration count
- output location

## Artifact Packaging

- Store result CSV/JSON files under `results/`.
- Keep heavyweight raw traces out of git and publish externally.
- Provide DOI or permanent URL for archived artifacts.
