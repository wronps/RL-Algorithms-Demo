from dataclasses import dataclass
from typing import Literal

State = tuple[int, int]
Action = Literal["up", "down", "left", "right"]

@dataclass
class GridworldConfig:
    rows: int = 5
    cols: int = 5

class Gridworld:
    def __init__(self, config: GridworldConfig):
        self.config = config
        self.rows = config.rows
        self.cols = config.cols

        self._validate_config()
    
    def _validate_config(self) -> None:
        if self.rows <= 0:
            raise ValueError("Rows must be a positive integer.")
        if self.cols <= 0:
            raise ValueError("Cols must be a positive integer.")
        
    @property
    def shape(self) -> tuple[int, int]:
        return self.rows, self.cols
    
    def get_states(self) -> list[State]:
        states: list[State] = []
        for row in range(self.rows):
            for col in range(self.cols):
                states.append((row, col))
        return states
    
    @property
    def state_count(self) -> int:
        return self.rows * self.cols
    
    def is_valid_state(self, state: State) -> bool:
        row, col = state
        return 0 <= row < self.rows and 0 <= col < self.cols
    
    def get_actions(self) -> list[Action]:
        return ["up", "down", "left", "right"]
    
    def get_next_state(self, state: State, action: Action) -> State:
        if action not in self.get_actions():
            raise ValueError(f"Invalid action: {action}")
        row, col = state
        if action == "up":
            candidate = (row - 1, col)
        elif action == "down":
            candidate = (row + 1, col)
        elif action == "left":
            candidate = (row, col - 1)
        else:
            candidate = (row, col + 1)
        if self.is_valid_state(candidate):
            return candidate
        return state