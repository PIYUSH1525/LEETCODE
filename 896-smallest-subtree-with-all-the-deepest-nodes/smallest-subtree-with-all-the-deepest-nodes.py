from typing import Optional, Tuple

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:      
        def dfs(node: Optional[TreeNode]) -> Tuple[Optional[TreeNode], int]:
            if node is None:
                return None, 0
            left_subtree, left_depth = dfs(node.left)
            right_subtree, right_depth = dfs(node.right)
            if left_depth > right_depth:
                return left_subtree, left_depth + 1
            if left_depth < right_depth:
                return right_subtree, right_depth + 1
            return node, left_depth + 1
        return dfs(root)[0]