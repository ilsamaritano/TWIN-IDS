from __future__ import annotations

import json
import subprocess
from pathlib import Path


def _run(module: str) -> None:
    subprocess.run(["python", "-m", module], check=True)


def main() -> None:
    modules = [
        "experiments.rq1_cost_efficiency",
        "experiments.rq2_detection_probability",
        "experiments.rq3_scalability",
        "experiments.rq4_sensitivity",
    ]

    for module in modules:
        _run(module)

    summary = {
        "status": "completed",
        "executed_modules": modules,
        "results_dir": "results",
    }
    Path("results").mkdir(parents=True, exist_ok=True)
    Path("results/summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
