from __future__ import annotations


def normalize_epss(epss_score: float) -> float:
    return min(max(float(epss_score), 0.0), 1.0)


def combined_exploitability(cvss_prob: float, epss_score: float, alpha: float = 0.5) -> float:
    cvss_prob = min(max(float(cvss_prob), 0.0), 1.0)
    epss_score = normalize_epss(epss_score)
    alpha = min(max(float(alpha), 0.0), 1.0)
    return alpha * cvss_prob + (1.0 - alpha) * epss_score
