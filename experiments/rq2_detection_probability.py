from __future__ import annotations

import argparse

from experiments.common import run_single_experiment, write_rows


def main() -> None:
    parser = argparse.ArgumentParser(description="RQ2: detection probability across IDS quality")
    parser.add_argument("--topology", default="data/topology_small_v31.json")
    parser.add_argument("--iterations", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--budget", type=int, default=2500)
    parser.add_argument("--out", default="results/rq2_detection_probability.csv")
    args = parser.parse_args()

    tp_levels = [0.65, 0.75, 0.85, 0.95]
    rows = []
    for tp in tp_levels:
        rows.append(
            run_single_experiment(
                topology_path=args.topology,
                budget=args.budget,
                iterations=args.iterations,
                seed=args.seed,
                sensor_true_positive_rate=tp,
            )
        )

    write_rows(args.out, rows)


if __name__ == "__main__":
    main()
