from __future__ import annotations

import argparse

from experiments.common import run_single_experiment, write_rows


def main() -> None:
    parser = argparse.ArgumentParser(description="RQ4: sensitivity analysis on random seeds")
    parser.add_argument("--topology", default="data/topology_small_v31.json")
    parser.add_argument("--iterations", type=int, default=1000)
    parser.add_argument("--budget", type=int, default=2500)
    parser.add_argument("--out", default="results/rq4_sensitivity.csv")
    args = parser.parse_args()

    seeds = [11, 22, 33, 44, 55]
    rows = []
    for seed in seeds:
        rows.append(
            run_single_experiment(
                topology_path=args.topology,
                budget=args.budget,
                iterations=args.iterations,
                seed=seed,
                sensor_true_positive_rate=0.85,
            )
        )

    write_rows(args.out, rows)


if __name__ == "__main__":
    main()
