import numpy as np


def man(hr, constants):
    return constants.ms * (
        1.0 / np.tanh(hr / constants.a)
        - constants.a / hr
    )

