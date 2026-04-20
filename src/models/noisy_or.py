from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class SensorDetection:
    sensor_id: str
    true_positive_rate: float


def noisy_or(detection_probs: Iterable[float]) -> float:
    product = 1.0
    for p in detection_probs:
        p = min(max(float(p), 0.0), 1.0)
        product *= 1.0 - p
    return 1.0 - product


def aggregate_sensor_detection(sensors: Iterable[SensorDetection]) -> float:
    return noisy_or(sensor.true_positive_rate for sensor in sensors)
