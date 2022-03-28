from TreeNode import TreeNode


class Solution:
    def maxDepth(self, root):
        # Base case
        if root is None:
            return 0

        # Recursive calls
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        # Post order visit
        return max(leftDepth, rightDepth) + 1

    def maxDepthIter(self, root):
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while len(stack):
            currentDepth, root = stack.pop()
            # Traverse
            if root is not None:
                depth = max(depth, currentDepth)
                stack.append((currentDepth + 1, root.left))
                stack.append((currentDepth + 1, root.right))

        return depth


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(6)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(8)

    s = Solution()
    print(s.maxDepthWithState(root))