from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def calculate_height(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left_height = calculate_height(node.left)
            right_height = calculate_height(node.right)
            if (left_height == -1 or 
                right_height == -1 or 
                abs(left_height - right_height) > 1):
                return -1  
            return 1 + max(left_height, right_height)
        return calculate_height(root) >= 0