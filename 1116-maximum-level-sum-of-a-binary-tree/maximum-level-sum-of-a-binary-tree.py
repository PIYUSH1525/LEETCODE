# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import Optional
from math import inf

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        max_sum = -inf
        current_level = 0
        result_level = 0
        while queue:
            current_level += 1
            level_sum = 0
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if max_sum < level_sum:
                max_sum = level_sum
                result_level = current_level
      
        return result_level