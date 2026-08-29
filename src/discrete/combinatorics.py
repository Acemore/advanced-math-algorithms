from typing import List, Set


def generate_arrangements(alphabet: List[str], k: int) -> List[str]:
    if k > len(alphabet) or k <= 0:
        return []

    result: List[str] = []

    def backtrack(current_token: List[str], used_indices: Set[int]):
        if len(current_token) == k:
            result.append("".join(current_token))
            return

        for i, char in enumerate(alphabet):
            if i not in used_indices:
                backtrack(current_token + [char], used_indices | {i})

    backtrack([], set())
    return result
