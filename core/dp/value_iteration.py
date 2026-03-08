from dataclasses import dataclass

@dataclass
class ValueIterationConfig:
    gamma: float = 0.95
    theta: float = 0.0001
    max_iterations: int = 200