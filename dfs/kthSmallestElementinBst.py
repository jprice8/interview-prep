from typing import Optional
from TreeNode import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            nonlocal res
            if node is None:
                return

            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        res = []
        dfs(root)
        return res[k - 1]

    def kthSmallestIter(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left 
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    s = Solution()
    print(s.kthSmallestIter(root, 1))