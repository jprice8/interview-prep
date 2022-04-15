from typing import Optional

from TreeNode import TreeNode


class Solution:
    def searchBst(self, root: Optional[TreeNode], val: int):
        def dfs(node):
            if node is None or node.val == val:
                return node 

            if val < node.val:
                return dfs(node.left)
            else:
                return dfs(node.right)
        return dfs(root)

if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    s = Solution()
    print(s.searchBst(root, 2))