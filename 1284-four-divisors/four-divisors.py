class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
      
        def get_divisor_sum_if_four(number: int) -> int:
            divisor = 2
            divisor_count = 2
            divisor_sum = number + 1
            while divisor <= number // divisor:
                if number % divisor == 0:
                    divisor_count += 1
                    divisor_sum += divisor
                    if divisor * divisor != number:
                        divisor_count += 1
                        divisor_sum += number // divisor
              
                divisor += 1
            return divisor_sum if divisor_count == 4 else 0
        return sum(get_divisor_sum_if_four(number) for number in nums)