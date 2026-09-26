from collections import deque

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


def ford_fulkerson(capacity_matrix: np.ndarray, source: int, sink: int) -> int:
    N = capacity_matrix.shape[0]
    residual_graph = capacity_matrix.copy()
    max_flow = 0
    parent = np.full(N, -1)

    def bfs_has_path(parent: np.ndarray):
        visited = np.full(N, False)
        parent.fill(-1)

        queue = deque([source])
        visited[source] = True

        while queue:
            u = queue.popleft()

            for v in range(N):
                if not visited[v] and residual_graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

                    if v == sink:
                        return True

        return False

    while bfs_has_path(parent):
        path_flow = np.inf
        v = sink

        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual_graph[u][v])
            v = u

        v = sink

        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = u

        max_flow += int(path_flow)

    return max_flow
