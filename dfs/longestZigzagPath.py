from enum import Enum
from TreeNode import TreeNode


class Direction(Enum):
    LEFT = 'left'
    RIGHT = 'right'


class Solution:
    def longestZigzagPath(self, root):
        longest = 0
        def dfs(node):
            nonlocal longest
            if node is None:
                return (0, 0)

            _, lr = dfs(node.left)
            rl, _ = dfs(node.right)

            longest = max(longest, lr + 1, rl + 1)
            return (lr + 1, rl + 1)

        dfs(root)
        return longest - 1

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(6)
    root.right.right.left.right = TreeNode(7)
    root.right.right.left.right.right = TreeNode(8)

    s = Solution()
    print(s.longestZigzagPath(root)) # 3