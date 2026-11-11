class Solution:
    def minimumCost(self,cost1: int,cost2: int,costBoth: int,need1: int,need2: int,) -> int:
        shared = min(need1, need2)
        separate = need1 * cost1 + need2 * cost2
        mixed = (
            shared * costBoth
            + (need1 - shared) * cost1
            + (need2 - shared) * cost2
        )
        both_only = max(need1, need2) * costBoth
        return min(separate, mixed, both_only)