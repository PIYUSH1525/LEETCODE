MAP_COUNT = [2] + [int(not (idx & 240) or not (idx & 60) or not (idx & 15))
                    for idx in range(1, 256)]
MAP_POWER = [0, 0, 1, 2, 4, 8, 16, 32, 64, 128, 0]

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats) -> int:
        map_count, map_power = MAP_COUNT, MAP_POWER
        rows  = collections.defaultdict(int)
        for row, seat in reservedSeats:
            rows[row] |= map_power[seat]
        return sum(map_count[row] for row in rows.values()) + 2*(n - len(rows))
