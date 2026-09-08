from src.discrete.combinatorics import generate_arrangements


def test_arrangements_count_and_uniqueness():
    secret_alphabet = ["A", "B", "C", "D", "E", "F"]
    token_length = 3

    tokens = generate_arrangements(secret_alphabet, token_length)

    assert len(tokens) == 120

    assert len(tokens) == len(set(tokens))

    assert len(tokens[0]) == 3


def test_invalid_cases():
    assert generate_arrangements(["A", "B"], 3) == []
    assert generate_arrangements(["A", "B"], 0) == []
