from __future__ import annotations


def cvss_base_to_probability(base_score: float) -> float:
    score = min(max(float(base_score), 0.0), 10.0)
    return score / 10.0


def parse_cvss_vector(vector: str) -> dict[str, str]:
    parsed: dict[str, str] = {}
    for token in vector.split("/"):
        if ":" not in token:
            continue
        key, value = token.split(":", 1)
        parsed[key] = value
    return parsed
