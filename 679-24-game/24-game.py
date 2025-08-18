class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        nums = [float(c) for c in cards]
        return self.helper(nums)

    def helper(self, nums: List[float]) -> bool:
        if len(nums) == 1:
            return abs(nums[0] - 24.0) < 1e-6

        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                a = nums[i]
                b = nums[j]
                
                next_round = []
                for k in range(n):
                    if k != i and k != j:
                        next_round.append(nums[k])

                operations = self.cal_operations(a, b)
                for op in operations:
                    next_round.append(op)
                    if self.helper(next_round):
                        return True
                    next_round.pop()
        
        return False

    def cal_operations(self, a: float, b: float) -> List[float]:
        results = []
        results.append(a + b)
        results.append(a - b)
        results.append(b - a)
        results.append(a * b)
        
        if b != 0:
            results.append(a / b)
        if a != 0:
            results.append(b / a)
            
        return results