from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CandidateSensor:
    sensor_id: str
    cost: int
    utility: float


def solve_01_knapsack(candidates: list[CandidateSensor], budget: int) -> list[CandidateSensor]:
    n = len(candidates)
    budget = max(0, int(budget))

    dp = [[0.0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item = candidates[i - 1]
        for w in range(budget + 1):
            without_item = dp[i - 1][w]
            with_item = -1.0
            if item.cost <= w:
                with_item = dp[i - 1][w - item.cost] + item.utility
            dp[i][w] = max(without_item, with_item)

    selected: list[CandidateSensor] = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item = candidates[i - 1]
            selected.append(item)
            w -= item.cost

    selected.reverse()
    return selected
