from typing import List, Optional
from TreeNode import TreeNode


class Solution:
    def boundary(self, root: Optional[TreeNode]) -> List[int]:
        def dfs_leftboundary(node):
            # if it's None or a leaf node
            if not node or not node.left and not node.right:
                return
            boundary.append(node.val)
            if node.left:
                dfs_leftboundary(node.left)
            else:
                dfs_leftboundary(node.right)

        def dfs_leaves(node):
            if not node:
                return 
            dfs_leaves(node.left)
            if node != root and not node.left and not node.right:
                boundary.append(node.val)
            dfs_leaves(node.right)

        def dfs_rightboundary(node):
            if not node or not node.left and not node.right:
                return 
            if node.right:
                dfs_rightboundary(node.right)
            else:
                dfs_rightboundary(node.left)
            boundary.append(node.val)

        if not root:
            return []
        boundary = [root.val]
        dfs_leftboundary(root.left)
        dfs_leaves(root)
        dfs_rightboundary(root.right)
        return boundary

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(8)

    root.right.left = TreeNode(6)
    root.right.left.left = TreeNode(9)
    root.right.left.right = TreeNode(10)

    s = Solution()
    print(s.boundary(root)) # [1, 2, 4, 7, 8, 9, 10, 6, 3]