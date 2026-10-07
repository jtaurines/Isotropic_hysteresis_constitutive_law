import numpy as np


def inv_man(x, constants):
    y = x / constants.ms

    return constants.a * (
        y * (3 - y**2) / (1 - y**2)
        - 0.488 * np.abs(y)**3.243 * y
        + 3.311
        * np.abs(y)**4.789
        * y
        * (np.abs(y) - 0.76)
        * (np.abs(y) - 1)
    )

