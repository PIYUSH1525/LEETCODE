class Solution:
    def maxDiff(self, num: int) -> int:
        str_num = str(num)
        max_num = str_num
        for digit in str_num:
            if digit != '9':
                max_num = max_num.replace(digit, '9')
                break  
        min_num = str_num
        if str_num[0] != '1':
            min_num = min_num.replace(str_num[0], '1')
        else:
            for digit in str_num[1:]:
                if digit not in '01':
                    min_num = min_num.replace(digit, '0')
                    break 
        return int(max_num) - int(min_num)