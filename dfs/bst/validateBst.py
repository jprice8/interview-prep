from TreeNode import TreeNode


class Solution:
    def validate(self, root):
        def dfs(node, min_value, max_value):
            if node is None:
                return True 

            # visit
            if not (min_value <= node.val <= max_value):
                return False

            # recursive calls
            return dfs(node.left, min_value, node.val) and dfs(node.right, node.val, max_value)

        return dfs(root, float('-inf'), float('inf'))


if __name__ == '__main__':
    root = TreeNode(7)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)

    root.right = TreeNode(11)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(13)

    s = Solution()
    print(s.validate(root))