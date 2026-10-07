import numpy as np
import matplotlib.pyplot as plt

from isomag.constants import Constants
from isomag.hysteresis import hysteresis_analytique


def main():
    constants = Constants()

    nb_points = 10_000
    Hmax = 10_000
    Hbas = 5_000

    h = np.concatenate([
        np.linspace(0.01, Hmax, nb_points),
        np.linspace(Hmax, -Hbas, nb_points),
        np.linspace(-Hbas, Hmax, nb_points),
        np.linspace(Hmax, -Hbas, nb_points),
    ])

    mr = 0

    m, hi, delta = hysteresis_analytique(
        h,
        mr,
        constants,
    )

    plt.figure()

    plt.plot(
        h * 1e-3,
        m * 1e-6,
        ".",
        markersize=4,
    )

    plt.grid()
    plt.xlabel(r"$H$ (kA/m)", fontsize=25)
    plt.ylabel(r"$M$ (MA/m)", fontsize=25)

    plt.savefig(
    "examples/hysteresis.png",
    dpi=300,
    bbox_inches="tight",
)




if __name__ == "__main__":
    main()

