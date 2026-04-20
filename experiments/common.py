from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
from random import Random

import networkx as nx

from src.engine.attack_paths import build_attack_graph
from src.engine.monte_carlo import SimulationConfig, run_attack_simulation
from src.models.knapsack import CandidateSensor, solve_01_knapsack
from src.utils.io import load_topology, save_csv


def _candidate_pool(graph: nx.DiGraph, seed: int = 42) -> list[CandidateSensor]:
    rng = Random(seed)
    betweenness = nx.betweenness_centrality(graph)
    candidates: list[CandidateSensor] = []

    for node in graph.nodes:
        role = str(graph.nodes[node].get("role", "host"))
        if role == "internet":
            continue
        cost = int(graph.nodes[node].get("sensor_cost", rng.randint(120, 600)))
        utility = float(betweenness.get(node, 0.0)) * 100.0 + rng.random() * 2.0
        candidates.append(CandidateSensor(sensor_id=str(node), cost=cost, utility=utility))

    return candidates


def choose_sensors(graph: nx.DiGraph, budget: int, seed: int = 42) -> set[str]:
    selected = solve_01_knapsack(_candidate_pool(graph, seed=seed), budget=budget)
    return {item.sensor_id for item in selected}


def default_assets(graph: nx.DiGraph) -> tuple[list[str], list[str]]:
    entry_nodes = [n for n, d in graph.nodes(data=True) if d.get("role") == "internet"]
    crown_jewels = [n for n, d in graph.nodes(data=True) if d.get("criticality", 0) >= 9]

    if not entry_nodes:
        entry_nodes = [next(iter(graph.nodes))]
    if not crown_jewels:
        crown_jewels = list(graph.nodes)[-2:]

    return entry_nodes, crown_jewels


def run_single_experiment(
    topology_path: str,
    budget: int,
    iterations: int,
    seed: int,
    sensor_true_positive_rate: float,
) -> dict:
    topology = load_topology(topology_path)
    graph = build_attack_graph(topology)
    sensor_nodes = choose_sensors(graph, budget=budget, seed=seed)
    entry_nodes, crown_jewels = default_assets(graph)

    result = run_attack_simulation(
        graph=graph,
        entry_nodes=entry_nodes,
        crown_jewels=crown_jewels,
        sensor_nodes=sensor_nodes,
        sensor_true_positive_rate=sensor_true_positive_rate,
        config=SimulationConfig(iterations=iterations, seed=seed),
    )

    payload = asdict(result)
    payload.update(
        {
            "budget": budget,
            "iterations": iterations,
            "seed": seed,
            "sensor_tp": sensor_true_positive_rate,
            "selected_sensors": len(sensor_nodes),
            "topology": Path(topology_path).name,
        }
    )
    return payload


def write_rows(output_path: str, rows: list[dict]) -> None:
    save_csv(output_path, rows)
