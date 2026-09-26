import numpy as np

from src.discrete.graphs import dijkstra, ford_fulkerson


def test_dijkstra_basic():
    graph = np.array(
        [
            [0, 5, 9],
            [5, 0, 2],
            [9, 2, 0],
        ]
    )
    result = dijkstra(graph, start_node=0)

    expected = [0.0, 5.0, 7.0]

    np.testing.assert_array_equal(result, expected)


def test_dijkstra_isolated():
    graph = np.array(
        [
            [0, 4, 0],
            [4, 0, 0],
            [0, 0, 0],
        ]
    )
    result = dijkstra(graph, start_node=0)

    expected = [0.0, 4.0, np.inf]

    np.testing.assert_array_equal(result, expected)


def test_ford_fulkerson_basic():
    capacity_matrix = np.array(
        [
            [0, 5, 3, 0],
            [0, 0, 1, 3],
            [0, 0, 0, 5],
            [0, 0, 0, 0],
        ]
    )

    assert ford_fulkerson(capacity_matrix, 0, 3) == 7


def test_ford_fulkerson_isolated():
    capacity_matrix = np.array(
        [
            [0, 5, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
    )

    assert ford_fulkerson(capacity_matrix, 0, 2) == 0
