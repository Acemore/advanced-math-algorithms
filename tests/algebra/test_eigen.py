import numpy as np
import pytest

from src.algebra.eigen import get_eigen_2x2


def test_get_eigen_2x2_basic():
    matrix = np.array([[4.0, 1.0], [3.0, 2.0]])
    lambdas, vectors = get_eigen_2x2(matrix)

    np.testing.assert_allclose(lambdas, [1.0, 5.0])
    np.testing.assert_allclose(
        vectors,
        [
            np.array([1.0, -3.0]),
            np.array([1.0, 1.0]),
        ],
    )


def test_get_eigen_2x2_lower_triangular_matrix():
    matrix = np.array([[3.0, 0.0], [4.0, 2.0]])
    lambdas, vectors = get_eigen_2x2(matrix)

    np.testing.assert_allclose(lambdas, [2.0, 3.0])
    np.testing.assert_allclose(
        vectors,
        [
            np.array([0.0, 1.0]),
            np.array([0.25, 1.0]),
        ],
    )


def test_get_eigen_2x2_diagonal_matrix():
    matrix = np.array([[3.0, 0.0], [0.0, 7.0]])
    lambdas, vectors = get_eigen_2x2(matrix)

    np.testing.assert_allclose(lambdas, [3.0, 7.0])
    np.testing.assert_allclose(
        vectors,
        [
            np.array([1.0, 0.0]),
            np.array([0.0, 1.0]),
        ],
    )


def test_get_eigen_2x2_not_square_matrix():
    matrix = np.array([[0, 1, 2], [2, 1, 0]])

    with pytest.raises(ValueError):
        get_eigen_2x2(matrix)


def test_get_eigen_2x2_complex_lambdas():
    matrix = np.array([[0, -1], [1, 0]])

    with pytest.raises(ValueError):
        get_eigen_2x2(matrix)
