class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        seen = []
        z = Counter(bulbs)
        for bub, val in z.items():
            if val%2 != 0 :
                seen.append(bub)
        return sorted(seen)