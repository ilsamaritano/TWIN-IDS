from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

from src.engine.attack_paths import build_attack_graph
from src.utils.io import load_topology


def _load_sensor_nodes(csv_path: str) -> set[str]:
    table = pd.read_csv(csv_path)
    if "node_id" in table.columns:
        return {str(x) for x in table["node_id"].tolist()}
    if "sensor_id" in table.columns:
        return {str(x) for x in table["sensor_id"].tolist()}
    return set()


def draw_twin(topology_path: str, placements_path: str, out_path: str) -> None:
    topology = load_topology(topology_path)
    graph = build_attack_graph(topology)
    sensor_nodes = _load_sensor_nodes(placements_path)

    pos = nx.spring_layout(graph, seed=7)

    node_colors = []
    node_sizes = []
    for node in graph.nodes:
        if node in sensor_nodes:
            node_colors.append("#c62828")
            node_sizes.append(700)
        elif graph.nodes[node].get("criticality", 0) >= 9:
            node_colors.append("#2e7d32")
            node_sizes.append(650)
        else:
            node_colors.append("#1565c0")
            node_sizes.append(430)

    plt.figure(figsize=(11, 7))
    nx.draw_networkx_edges(graph, pos, alpha=0.25, arrows=True, arrowsize=12)
    nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=node_sizes)
    nx.draw_networkx_labels(graph, pos, font_size=8)
    plt.title("TWIN-IDS: Digital Twin with Risk-Aware Sensor Placement")
    plt.axis("off")

    output = Path(out_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(output, dpi=240)
    plt.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Visualize digital twin and IDS placements")
    parser.add_argument("--topology", default="data/topology_small_v31.json")
    parser.add_argument("--placements", default="data/ids_sensor_profiles.csv")
    parser.add_argument("--out", default="results/twin_layout.png")
    args = parser.parse_args()

    draw_twin(args.topology, args.placements, args.out)


if __name__ == "__main__":
    main()
