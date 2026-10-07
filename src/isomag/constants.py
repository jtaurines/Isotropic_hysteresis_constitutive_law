from dataclasses import dataclass
import numpy as np


@dataclass
class Constants:
    ms: float = 1_500_000
    a: float = 1_000
    Hc: float = 3_000
    epsilon: float = 1e-4

    @property
    def chi_eq(self) -> float:
        return -self.ms / (np.log(self.epsilon) * self.Hc)

