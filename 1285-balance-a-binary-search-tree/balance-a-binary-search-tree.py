class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder_traversal(node: TreeNode) -> None:
            if node is None:
                return
            inorder_traversal(node.left)
            sorted_values.append(node.val)
            inorder_traversal(node.right)
      
        def build_balanced_bst(left_idx: int, right_idx: int) -> TreeNode:
            if left_idx > right_idx:
                return None
            mid_idx = (left_idx + right_idx) // 2
            left_subtree = build_balanced_bst(left_idx, mid_idx - 1)
            right_subtree = build_balanced_bst(mid_idx + 1, right_idx)
            return TreeNode(sorted_values[mid_idx], left_subtree, right_subtree)
        sorted_values = []
        inorder_traversal(root)
        return build_balanced_bst(0, len(sorted_values) - 1)