from typing import List
from collections import defaultdict


class Solution:
    """Solution for finding all unique combinations that sum to a target.

    You are given an array of distinct integers `candidates` and a target integer
    `target`. Return a list of all unique combinations of `candidates` where the
    chosen numbers sum to `target`. The same number may be chosen from
    `candidates` an unlimited number of times, and each combination should be
    returned in any order.:contentReference[oaicite:0]{index=0}
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """Returns all unique combinations of candidates that sum to target.

        Args:
            candidates (List[int]): The list of distinct candidate values.
            target (int): The target sum to achieve.

        Returns:
            List[List[int]]: A list of lists, each inner list is a unique
                combination of candidates that sum to `target`.
        """
        # num -> combinations summed
        # int -> List[List[int]]
        sum_to_combos = defaultdict(list)
        sum_to_combos[0] = [[]]

        for num in candidates:
            new_entries = defaultdict(list)
            for combo_sum, combos in sum_to_combos.items():
                for combo in combos:
                    mult = 1
                    while combo_sum + mult * num <= target:
                        new_entries[combo_sum + mult * num].append(
                            combo + [num for _ in range(mult)]
                        )
                        mult += 1

            for k, v in new_entries.items():
                sum_to_combos[k].extend(v)

        return sum_to_combos[target]
