from typing import Union, Dict
from dataclasses import dataclass
import numpy as np

@dataclass
class Difficulty:
    num_items: int
    percent_better_than_expected_value: int

@dataclass
class Challenge:
    seed: int
    difficulty: Difficulty
    weights: np.ndarray
    values: np.ndarray
    max_weight: int
    min_value: int

    def verifySolution(self, solution: list) -> bool:
        try:
            selected_items = np.array(solution, dtype=int)
            if len(selected_items.shape) != 1 or len(selected_items) > len(self.weights) or set(selected_items) - set(range(len(self.weights))) or len(selected_items) != len(set(selected_items)):
                raise Exception("Invalid items. Expecting a subset of [0, ..., num_items - 1]")        
            total_weight = np.sum(self.weights[selected_items])
            total_value = np.sum(self.values[selected_items])
            return total_weight <= self.max_weight and total_value >= self.min_value
        except Exception as e:
            raise Exception("Invalid solution") from e

    @classmethod
    def generateInstance(cls, seed: int, difficulty: Union[Difficulty, Dict[str, int]]):
        if isinstance(difficulty, dict):
            difficulty = Difficulty(**difficulty)
        np.random.seed(seed)
        weights = np.random.randint(1, 50, size=difficulty.num_items)
        values = np.random.randint(1, 50, size=difficulty.num_items)
        max_weight = int(np.sum(weights) / 2)
        min_value = int(np.sum(values) / 2 * (1 + difficulty.percent_better_than_expected_value / 100))
        return cls(
            seed=seed,
            difficulty=difficulty,
            weights=weights,
            values=values,
            max_weight=max_weight,
            min_value=min_value
        )