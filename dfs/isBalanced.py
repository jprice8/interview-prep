from TreeNode import TreeNode


class Solution:
    def isBalanced(self, root):
        def dfs(node):
            if node is None:
                return 0

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            if leftHeight == -1 or rightHeight == -1:
                return -1

            if abs(leftHeight - rightHeight) > 1:
                return -1

            return max(leftHeight, rightHeight) + 1
        return dfs(root) != -1


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.left = TreeNode(2)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)

    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)

    s = Solution()
    print(s.isBalanced(root))