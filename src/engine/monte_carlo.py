from __future__ import annotations

from dataclasses import dataclass
from random import Random

import networkx as nx


@dataclass(frozen=True)
class SimulationConfig:
    iterations: int = 1000
    seed: int = 42


@dataclass(frozen=True)
class SimulationResult:
    compromise_rate: float
    detection_rate: float
    mean_compromised_nodes: float


def run_attack_simulation(
    graph: nx.DiGraph,
    entry_nodes: list[str],
    crown_jewels: list[str],
    sensor_nodes: set[str],
    sensor_true_positive_rate: float,
    config: SimulationConfig,
) -> SimulationResult:
    rng = Random(config.seed)
    detections = 0
    successful_compromises = 0
    compromised_sum = 0

    entry_candidates = [n for n in entry_nodes if n in graph]
    if not entry_candidates:
        raise ValueError("No valid entry nodes found in graph.")

    for _ in range(config.iterations):
        start = rng.choice(entry_candidates)
        compromised = {start}
        frontier = [start]
        detected = False

        while frontier:
            node = frontier.pop()
            if node in sensor_nodes and rng.random() < sensor_true_positive_rate:
                detected = True

            for neighbor in graph.successors(node):
                if neighbor in compromised:
                    continue
                edge_prob = float(graph[node][neighbor].get("exploit_prob", 0.5))
                if rng.random() < edge_prob:
                    compromised.add(neighbor)
                    frontier.append(neighbor)

        compromised_sum += len(compromised)
        if detected:
            detections += 1
        if any(asset in compromised for asset in crown_jewels):
            successful_compromises += 1

    return SimulationResult(
        compromise_rate=successful_compromises / config.iterations,
        detection_rate=detections / config.iterations,
        mean_compromised_nodes=compromised_sum / config.iterations,
    )
