from __future__ import annotations

from typing import Iterable

import networkx as nx


def build_attack_graph(topology: dict) -> nx.DiGraph:
    graph = nx.DiGraph()

    for node in topology["nodes"]:
        graph.add_node(node["id"], **node)

    for edge in topology["edges"]:
        graph.add_edge(
            edge["source"],
            edge["target"],
            exploit_prob=float(edge.get("exploit_prob", 0.5)),
            cve=str(edge.get("cve", "CVE-UNKNOWN")),
        )

    return graph


def enumerate_paths(
    graph: nx.DiGraph,
    sources: Iterable[str],
    targets: Iterable[str],
    cutoff: int = 5,
) -> list[list[str]]:
    all_paths: list[list[str]] = []
    for src in sources:
        for dst in targets:
            if src in graph and dst in graph and src != dst:
                for path in nx.all_simple_paths(graph, source=src, target=dst, cutoff=cutoff):
                    all_paths.append(path)
    return all_paths


def path_success_probability(graph: nx.DiGraph, path: list[str]) -> float:
    if len(path) < 2:
        return 0.0

    p = 1.0
    for u, v in zip(path[:-1], path[1:]):
        p *= float(graph[u][v].get("exploit_prob", 0.5))
    return p
