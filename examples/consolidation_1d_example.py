
"""
Terzaghi 1D Consolidation — Isochrone Generator.

Author: Raul Galdeano Pazos
Project: Civil Engineering Data Analysis Toolbox
"""

from pathlib import Path
import sys

import numpy as np
import matplotlib.pyplot as plt

# Locate the repository and source package.
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from civil_engineering_toolbox.geotechnics.consolidation_1d import (
    porewater_pressure,
)


def main():
    """Generate normalized consolidation isochrones."""

    # Normalized spatial discretization.
    z = np.linspace(0.0, 1.0, 200)

    # Dimensionless time factors.
    time_factors = [
        0.01, 0.02, 0.05, 0.1,
        0.2, 0.5, 1.0, 2.0
    ]

    # Initialize visualization.
    fig, ax = plt.subplots(figsize=(9, 7))

    for time_factor in time_factors:

        pressure = porewater_pressure(
            z=z,
            time_factor=time_factor,
            n_terms=80
        )

        ax.plot(
            pressure,
            1.0 - z,
            linewidth=2,
            label=f"T = {time_factor:g}"
        )

    # Scientific plot formatting.
    ax.set_xlabel(
        "Normalized excess porewater pressure (W)"
    )

    ax.set_ylabel("Normalized coordinate (1 - Z)")

    ax.set_title(
        "Terzaghi 1D Consolidation — Isochrones"
    )

    ax.set_xlim(left=0)
    ax.set_ylim(0, 1)

    ax.grid(True, alpha=0.3)
    ax.legend(loc="best")

    fig.tight_layout()

    # Create output directory if necessary.
    output_dir = ROOT / "outputs"
    output_dir.mkdir(exist_ok=True)

    output_path = (
        output_dir / "terzaghi_1d_isochrones.png"
    )

    # Save the figure before displaying it.
    fig.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight"
    )

    print(f"Figure saved to: {output_path}")

    plt.show()


if __name__ == "__main__":
    main()
