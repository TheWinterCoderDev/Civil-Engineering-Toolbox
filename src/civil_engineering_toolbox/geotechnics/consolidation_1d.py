
"""
MATLAB Survival Project Companion
Civil Engineering Data Analysis Toolbox

Module: One-Dimensional Consolidation
Theory: Terzaghi's Consolidation Theory

Author: Raul Galdeano Pazos
"""

import numpy as np


def porewater_pressure(z, time_factor, n_terms=80):
    """
    Compute normalized excess porewater pressure using
    the Fourier-series solution of Terzaghi's 1D
    consolidation equation.

    Assumptions
    -----------
    - Homogeneous saturated soil.
    - Constant coefficient of consolidation.
    - Uniform initial excess porewater pressure.
    - Double drainage, using half-layer symmetry.

    Parameters
    ----------
    z : float or array_like
        Normalized depth coordinate, between 0 and 1.
        Zero is the drained boundary and one is
        the symmetry plane.

    time_factor : float or array_like
        Dimensionless time factor:

            T = cv * t / Hdr**2

        Must be nonnegative.

    n_terms : int, optional
        Number of Fourier series terms.
        Default: 80.

    Returns
    -------
    numpy.ndarray
        Normalized excess porewater pressure W(z, T).

    Notes
    -----
    The infinite series is approximated using a finite
    number of terms. Numerical accuracy depends on
    convergence, especially close to T = 0.
    """

    # Validate number of series terms.
    if (
        isinstance(n_terms, (bool, np.bool_))
        or not isinstance(n_terms, (int, np.integer))
        or n_terms < 1
    ):
        raise ValueError(
            "n_terms must be a positive integer."
        )

    # Convert input parameters to numerical arrays.
    z = np.asarray(z, dtype=float)
    time_factor = np.asarray(time_factor, dtype=float)

    # Validate finite numerical inputs.
    if not np.all(np.isfinite(z)):
        raise ValueError(
            "Normalized depth must contain finite values."
        )

    if not np.all(np.isfinite(time_factor)):
        raise ValueError(
            "Time factor must contain finite values."
        )

    # Validate the normalized depth domain.
    if np.any((z < 0) | (z > 1)):
        raise ValueError(
            "Normalized depth must be between 0 and 1."
        )

    # Validate dimensionless time.
    if np.any(time_factor < 0):
        raise ValueError(
            "Time factor must be nonnegative."
        )

    # Match input array dimensions.
    z, time_factor = np.broadcast_arrays(
        z, time_factor
    )

    # Initialize the Fourier series.
    result = np.zeros_like(z, dtype=float)

    # Compute the truncated Fourier series.
    for n in range(n_terms):

        k = 2 * n + 1

        coefficient = 4.0 / (k * np.pi)

        exponential = np.exp(
            -(k * np.pi) ** 2 * time_factor / 4.0
        )

        spatial = np.sin(
            k * np.pi * z / 2.0
        )

        result += coefficient * exponential * spatial

    return result
