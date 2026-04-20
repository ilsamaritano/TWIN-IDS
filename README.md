# TWIN-IDS: Twin-driven IDS Placement for Cost-aware Detection

A reproducible research codebase for evaluating **risk-aware intrusion detection system (IDS) sensor placement** on security (network) digital twins.

This repository provides an end-to-end implementation template for:
- attack graph and probabilistic path modeling
- Monte Carlo simulation of compromise propagation
- budget-aware sensor placement optimization
- experiment pipelines aligned with research questions (RQ1-RQ4)

The project is structured for high-level cybersecurity venues (ESORICS, CCS, USENIX Security, NDSS) and emphasizes reproducibility, clear experiment mapping, and modular design.

## Abstract

TWIN-IDS models enterprise and industrial network twins as probabilistic attack surfaces and optimizes IDS placement under a fixed budget. The framework combines path-level risk estimation, noisy-OR style detection aggregation, and knapsack-based optimization to identify high-value sensor deployments. The code supports synthetic and anonymized real-like topologies, enabling controlled comparisons across cost-efficiency, scalability, and sensitivity analyses.

## Repository Layout

```text
.
├── data/                         # Input datasets and example topologies
├── docker/                       # Reproducible container environment
├── experiments/                  # Scripts mapped to paper RQs
├── notebooks/                    # Analysis and plotting notebooks
├── results/                      # Generated outputs (CSV/JSON/figures)
└── src/
    ├── engine/                   # Attack-path and Monte Carlo simulation engine
    ├── models/                   # Noisy-OR and optimization models
    └── utils/                    # Parsing, I/O, visualization helpers
```

## Hardware Requirements

Minimum setup for lightweight runs (small topology, ~31 nodes):
- CPU: 2+ cores
- RAM: 4 GB
- Disk: 1 GB free

Recommended for medium/large experiments (up to 10k nodes with repeated simulations):
- CPU: 8+ cores
- RAM: 32 GB+
- Disk: 20 GB free (for raw outputs and intermediate traces)

## Software Requirements

- Python 3.11+
- pip 23+
- Optional: Docker 24+

## Installation

### Option 1: Local venv

```bash
python -m venv .venv
. .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

### Option 2: Docker

```bash
docker build -t twin-ids -f docker/Dockerfile .
docker run --rm -it -v "$PWD/results:/app/results" twin-ids python -m experiments.rq1_cost_efficiency
```

## Quick Start (under 5 minutes)

Run a lightweight benchmark using the included small topology:

```bash
python -m experiments.rq1_cost_efficiency \
  --topology data/topology_small_v31.json \
  --iterations 1000 \
  --budget 2500 \
  --out results/rq1_small.csv
```

Visualize one deployment result:

```bash
python -m src.utils.visualize_twin \
  --topology data/topology_small_v31.json \
  --placements data/ids_sensor_profiles.csv \
  --out results/twin_layout.png
```

## Reproducing Paper Results

| Paper Artifact | Script | Output |
| :-- | :-- | :-- |
| RQ1: Cost-Efficiency | `python -m experiments.rq1_cost_efficiency` | `results/rq1_*.csv` |
| RQ2: Detection Probability | `python -m experiments.rq2_detection_probability` | `results/rq2_*.csv` |
| RQ3: Scalability | `python -m experiments.rq3_scalability` | `results/rq3_*.csv` |
| RQ4: Sensitivity | `python -m experiments.rq4_sensitivity` | `results/rq4_*.csv` |
| Full pipeline | `python -m experiments.run_all` | `results/summary.json` |

Use explicit seeds in scripts for deterministic re-runs.

## Data Policy and Openness

- Keep sensitive infrastructure details anonymized.
- Replace direct identifiers (hostnames, IP addresses, organization names) before release.
- For large datasets, store artifacts in Zenodo/Figshare and reference DOIs in this README.
- The `data/` folder contains only sanitized and synthetic examples by default.


## Citation

If accepted, include the final BibTeX cite here:

```bibtex
@inproceedings{twinids2026,
  title={TWIN-IDS: Twin-driven IDS Placement for Cost-aware Detection},
  author={Sammartino, V. and Baiardi, F. and Ruggieri, S.},
  booktitle={Proceedings of the 31st European Symposium on Research in Computer Security (ESORICS) 2026},
  year={2026}
}
```

## License

Distributed under the Apache-2.0 License. See `LICENSE`.

## Contact

During anonymous review: use the submission system discussion channel only.
After acceptance: add project maintainer contact and issue templates.
