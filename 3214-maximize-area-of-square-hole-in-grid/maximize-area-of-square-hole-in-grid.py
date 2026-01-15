class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
      
        def find_max_consecutive_gap(bars: List[int]) -> int:
            bars.sort()
            max_consecutive = 1
            current_consecutive = 1
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    current_consecutive += 1
                    max_consecutive = max(max_consecutive, current_consecutive)
                else:
                    current_consecutive = 1
            return max_consecutive + 1
        max_horizontal_gap = find_max_consecutive_gap(hBars)
        max_vertical_gap = find_max_consecutive_gap(vBars)
        max_square_side = min(max_horizontal_gap, max_vertical_gap)
        return max_square_side ** 2