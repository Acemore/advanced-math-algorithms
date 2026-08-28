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
                used_indices.add(i)
                current_token.append(char)

                backtrack(current_token, used_indices)

                current_token.pop()
                used_indices.remove(i)

    backtrack([], set())
    return result
