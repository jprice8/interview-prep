from TreeNode import TreeNode


class Solution:
    def maxValue(self, root):
        if root is None:
            return 0
        
        left = self.maxValue(root.left)
        right = self.maxValue(root.right)

        return max(root.val, left, right)

    def maxValueWithGlobal(self, root):
        MAX_VAL = float('-inf')
        def dfs(node):
            nonlocal MAX_VAL
            if node is None:
                return 

            if node.val > MAX_VAL:
                MAX_VAL = node.val 

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return MAX_VAL


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(11)

    s = Solution()
    # print(s.maxValue(root))
    print(s.maxValueWithGlobal(root))