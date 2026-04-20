from __future__ import annotations

import argparse

from experiments.common import run_single_experiment, write_rows


def main() -> None:
    parser = argparse.ArgumentParser(description="RQ1: cost-efficiency under varying budget")
    parser.add_argument("--topology", default="data/topology_small_v31.json")
    parser.add_argument("--iterations", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--budget", type=int, default=2500)
    parser.add_argument("--out", default="results/rq1_cost_efficiency.csv")
    args = parser.parse_args()

    budget_levels = [max(100, args.budget // 2), args.budget, args.budget * 2]
    rows = []
    for budget in budget_levels:
        rows.append(
            run_single_experiment(
                topology_path=args.topology,
                budget=budget,
                iterations=args.iterations,
                seed=args.seed,
                sensor_true_positive_rate=0.85,
            )
        )

    write_rows(args.out, rows)


if __name__ == "__main__":
    main()
