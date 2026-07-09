from typing import List


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        group_id = [0] * n

        current_group = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                current_group += 1

            group_id[i] = current_group
        result = [group_id[u] == group_id[v] for u, v in queries]

        return result