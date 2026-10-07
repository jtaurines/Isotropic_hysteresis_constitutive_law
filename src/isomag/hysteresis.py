import numpy as np
from scipy.optimize import minimize_scalar

from .man import man
from .inv_man import inv_man


def hysteresis_analytique(h, mr, constants):
    h = np.asarray(h, dtype=float)

    n = len(h)

    m = np.empty(n)
    hi = np.empty(n)
    delta = np.empty(n)

    # Initialisation avec la magnétisation rémanente
    m[0] = mr
    hi[0] = h[0] - inv_man(mr, constants)

    m0 = m[0]
    hi0 = hi[0]

    delta[0] = np.sign(h[0])

    for i in range(1, n):

        dh = h[i] - h[i - 1]

        # Équivalent de :
        # delta(i)=dh/abs(dh)
        if dh == 0:
            delta[i] = delta[i - 1]
        else:
            delta[i] = np.sign(dh)

        m0 = m[i - 1]
        hi0 = hi[i - 1]

        def objective(x):
            term = (
                m0
                + constants.ms / np.log(constants.epsilon)
                * delta[i]
                * (
                    np.log(
                        1 - delta[i] * x / constants.Hc
                    )
                    - np.log(
                        1 - delta[i] * hi0 / constants.Hc
                    )
                )
            )

            return abs(term - man(h[i] - x, constants))

        result = minimize_scalar(
            objective,
            bounds=(-constants.Hc, constants.Hc),
            method="bounded",
        )

        hi[i] = result.x

        hr = h[i] - hi[i]

        m[i] = man(hr, constants)

    return m, hi, delta

