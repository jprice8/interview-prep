from TreeNode import TreeNode


class Solution:
    def invert(self, root):
        def dfs(node):
            if node is None:
                return 

            leftNode = node.left
            node.left = node.right
            node.right = leftNode

            dfs(node.left)
            dfs(node.right)

        dfs(root)


if __name__ == '__main__':
    root = TreeNode(7)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)

    root.right = TreeNode(11)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(13)

    s = Solution()
    print(s.invert(root))