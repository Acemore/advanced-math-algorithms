import math
from typing import List, Tuple

import numpy as np


def get_eigen_2x2(matrix: np.ndarray) -> Tuple[List[float], List[np.ndarray]]:
    if matrix.shape != (2, 2):
        raise ValueError("Matrix must be 2x2")

    b = -(matrix[0, 0] + matrix[1, 1])
    c = matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]

    D = b**2 - 4 * c

    if D < 0:
        raise ValueError("Complex eigenvalues are not supported")

    lambda_1 = (-b - math.sqrt(D)) / 2
    lambda_2 = (-b + math.sqrt(D)) / 2
    lambdas = [lambda_1, lambda_2]

    vectors = []

    if matrix[0, 1] != 0:
        x_1 = 1.0

        for lambda_ in lambdas:
            x_2 = -(matrix[0, 0] - lambda_) / matrix[0, 1]
            vectors.append(np.array([x_1, x_2]))
    else:
        if matrix[1, 0] != 0:
            for lambda_ in lambdas:
                x_2 = 1.0
                x_1 = -(matrix[1, 1] - lambda_) / matrix[1, 0]

                vectors.append(np.array([x_1, x_2]))
        else:
            vectors.append(np.array([1.0, 0.0]))
            vectors.append(np.array([0.0, 1.0]))

    return lambdas, vectors
