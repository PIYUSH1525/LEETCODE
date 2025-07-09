from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        freeArray = [0] * (n + 1)
        freeArray[0] = startTime[0]
        for i in range(1, n):
            freeArray[i] = startTime[i] - endTime[i - 1]
        freeArray[n] = eventTime - endTime[n - 1]
        
        maxSum = 0
        currSum = 0
        left = 0
        for right in range(len(freeArray)):
            currSum += freeArray[right]
            while right - left + 1 > k + 1:
                currSum -= freeArray[left]
                left += 1
            
            maxSum = max(maxSum, currSum)
        
        return maxSum
