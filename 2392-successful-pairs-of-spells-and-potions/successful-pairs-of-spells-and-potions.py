class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        result = []

        for spell in spells:
            required = math.ceil(success / spell)
            idx = bisect_left(potions, required)
            result.append(n - idx)

        return result
        