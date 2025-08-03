class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        
        n = len(fruits)
        if n == 0:
            return 0
        indices = [fruit[0] for fruit in fruits]
        prefix_sum = [0] * n
        prefix_sum[0] = fruits[0][1]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + fruits[i][1]

        def get_fruits_in_range(start, end):
            left_idx = bisect.bisect_left(indices, start)
            right_idx = bisect.bisect_right(indices, end) - 1

            if left_idx > right_idx:
                return 0
            
            total_fruits = prefix_sum[right_idx] - (prefix_sum[left_idx - 1] if left_idx > 0 else 0)
            return total_fruits

        max_fruits = 0
        for d in range(k // 2 + 1):
            left_dist_1, right_dist_1 = d, k - 2 * d
            start_range_1 = startPos - left_dist_1
            end_range_1 = startPos + right_dist_1
            max_fruits = max(max_fruits, get_fruits_in_range(start_range_1, end_range_1))
            right_dist_2, left_dist_2 = d, k - 2 * d
            start_range_2 = startPos - left_dist_2
            end_range_2 = startPos + right_dist_2
            max_fruits = max(max_fruits, get_fruits_in_range(start_range_2, end_range_2))
            
        return max_fruits
