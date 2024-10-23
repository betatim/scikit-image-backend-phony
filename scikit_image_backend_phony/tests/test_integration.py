import pytest

import numpy as np
from skimage.metrics import mean_squared_error, normalized_root_mse
from skimage.util._backends import DispatchNotification


def some_function():
    mean_squared_error(np.asarray([0.0, 0.5]), np.asarray([0.0, 0.9]))


def test_dispatching():
    with pytest.warns(
        DispatchNotification,
        match="Call to.*:mean_squared_error' was dispatched",
    ):
        mean_squared_error(np.asarray([0.0, 0.5]), np.asarray([0.0, 0.9]))

    # This should not be dispatched as this backend
    # does not implement it
    normalized_root_mse(np.asarray([0.0, 0.5]), np.asarray([0.0, 0.9]))


def test_warnings():
    with pytest.warns(
        DispatchNotification,
        match="Call to.*:mean_squared_error' was dispatched",
    ):
        some_function()

    # The warning should not be repeated after the first call
    some_function()