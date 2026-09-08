import numpy as np


def dijkstra(matrix: np.ndarray, start_node: int) -> np.ndarray:
    N = matrix.shape[0]

    distances = np.full(N, np.inf)
    distances[start_node] = 0

    visited = np.full(N, False)

    for i in range(N):
        temp_distances = np.where(visited, np.inf, distances)
        current_node = int(np.argmin(temp_distances))

        if distances[current_node] == np.inf:
            break

        visited[current_node] = True

        for neighbor in range(N):
            if matrix[current_node][neighbor] > 0 and not visited[neighbor]:
                new_dist = distances[current_node] + matrix[current_node][neighbor]

                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist

    return distances
