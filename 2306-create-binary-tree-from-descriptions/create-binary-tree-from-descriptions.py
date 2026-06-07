class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes, children = {}, set()

        for description in descriptions:
            (val, child, is_left) = description
            node = None

            if val in nodes:
                node = nodes[val]
            else:
                node = TreeNode(val)
                nodes[val] = node

            child_node = None

            if child in nodes:
                child_node = nodes[child]
            else:
                child_node = TreeNode(child)
                nodes[child] = child_node

            children.add(child)

            if is_left == 1:
                node.left = child_node
            else:
                node.right = child_node

        for node in nodes.keys():
            if node not in children:
                return nodes[node]

        return None