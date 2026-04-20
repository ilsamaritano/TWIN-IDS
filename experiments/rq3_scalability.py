from __future__ import annotations

import argparse

from experiments.common import run_single_experiment, write_rows


def main() -> None:
    parser = argparse.ArgumentParser(description="RQ3: scalability vs Monte Carlo iterations")
    parser.add_argument("--topology", default="data/topology_small_v31.json")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--budget", type=int, default=2500)
    parser.add_argument("--out", default="results/rq3_scalability.csv")
    args = parser.parse_args()

    iteration_levels = [250, 500, 1000, 5000]
    rows = []
    for iterations in iteration_levels:
        rows.append(
            run_single_experiment(
                topology_path=args.topology,
                budget=args.budget,
                iterations=iterations,
                seed=args.seed,
                sensor_true_positive_rate=0.85,
            )
        )

    write_rows(args.out, rows)


if __name__ == "__main__":
    main()
