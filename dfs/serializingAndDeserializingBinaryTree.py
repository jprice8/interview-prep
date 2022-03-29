from collections import deque
from TreeNode import TreeNode


class Codec:
    def serialize(self, root: TreeNode) -> str:
        node_chars = []
        def dfs(node, node_chars):
            if node is None:
                node_chars.append('N')
                return 

            # Preorder visit
            node_chars.append(str(node.val))

            # Recursive calls
            dfs(node.left, node_chars)
            dfs(node.right, node_chars)

        dfs(root, node_chars)
        return ' '.join(node_chars)

    def deserialize(self, tree_string: str) -> TreeNode:
        def dfs(nodes):
            val = next(nodes)
            if val == 'N':
                return
            tree_node = TreeNode(int(val))
            tree_node.left = dfs(nodes)
            tree_node.right = dfs(nodes)
            return tree_node

        # Iterator returns a token each time we call 'next'
        return dfs(iter(tree_string.split()))


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    c = Codec()
    tree_string = c.serialize(root)
    print(tree_string)
    print(c.deserialize(tree_string))
    