class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        min_num = int(num_str.replace(num_str[0], '0'))
        for digit in num_str:
            if digit != '9':
                max_num = int(num_str.replace(digit, '9'))
                return max_num - min_num
        return num - min_num
        