
"""Tests for Terzaghi's 1D consolidation solver."""

import numpy as np
import pytest

from civil_engineering_toolbox.geotechnics.consolidation_1d import (
    porewater_pressure,
)


def test_drained_boundary():
    """Excess pressure must vanish at the drained boundary."""

    times = np.array([0.0, 0.1, 0.5, 1.0])
    result = porewater_pressure(0.0, times)

    np.testing.assert_allclose(
        result, np.zeros(4), atol=1e-12
    )


def test_pressure_decreases_with_time():
    """Excess pressure decreases during consolidation."""

    values = [
        float(porewater_pressure(0.5, t))
        for t in [0.05, 0.2, 0.5]
    ]

    assert values[0] > values[1] > values[2] > 0


def test_long_time_approximation():
    """At large times, the first Fourier term dominates."""

    z = 0.5
    t = 2.0

    expected = (
        4 / np.pi
        * np.exp(-np.pi**2 * t / 4)
        * np.sin(np.pi * z / 2)
    )

    actual = porewater_pressure(z, t)

    assert actual == pytest.approx(
        expected, rel=1e-10
    )


def test_vectorized_depth():
    """Solver must support multiple spatial positions."""

    z = np.linspace(0.0, 1.0, 25)

    result = porewater_pressure(z, 0.1)

    assert result.shape == z.shape
    assert np.all(np.isfinite(result))


def test_invalid_depth():
    """Depth must remain in the normalized domain."""

    with pytest.raises(ValueError):
        porewater_pressure(-0.1, 0.1)

    with pytest.raises(ValueError):
        porewater_pressure(1.2, 0.1)


def test_negative_time():
    """Negative time factors are not physically admissible."""

    with pytest.raises(ValueError):
        porewater_pressure(0.5, -0.1)


def test_invalid_series_terms():
    """The number of Fourier terms must be positive."""

    with pytest.raises(ValueError):
        porewater_pressure(0.5, 0.1, n_terms=0)


def test_nonfinite_inputs():
    """NaN and infinite input values must be rejected."""

    with pytest.raises(ValueError):
        porewater_pressure(np.nan, 0.1)

    with pytest.raises(ValueError):
        porewater_pressure(0.5, np.inf)
