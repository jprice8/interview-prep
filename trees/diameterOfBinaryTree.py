from typing import Optional
from nodeDepths import BinaryTreeNode


class Solution:
    def diameter(self, root: Optional[BinaryTreeNode]) -> int:
        diameter = 0
        def dfs(node, length=0):
            nonlocal diameter
            if node is None:
                return 0
            
            maxLeft = dfs(node.left)
            maxRight = dfs(node.right)

            diameter = max(diameter, maxLeft + maxRight)

            return max(maxLeft, maxRight) + 1
        
        dfs(root)
        return diameter


if __name__ == '__main__':
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(3)
    node4 = BinaryTreeNode(4)
    node5 = BinaryTreeNode(5)

    node1.left = node2 
    node1.right = node3 

    node2.left = node4 
    node2.right = node5

    # node1 = BinaryTreeNode(1)
    # node2 = BinaryTreeNode(2)

    # node1.left = node2

    s = Solution()
    print(s.diameter(node1))