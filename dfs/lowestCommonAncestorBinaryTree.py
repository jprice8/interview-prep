from TreeNode import TreeNode


class Solution:
    def lowestCommonAncestorBinaryTree(self, root: TreeNode, p: int, q: int) -> TreeNode:
        def dfs(node, p, q):
            if node is None:
                return TreeNode(-1)

            # Recursive calls
            leftResult = dfs(node.left, p, q)
            rightResult = dfs(node.right, p, q)

            # Postorder visit
            if ((leftResult.val != -1 and rightResult.val != -1) or 
                p.val == node.val or 
                q.val == node.val):
                return node

            if leftResult.val != -1:
                return leftResult
            if rightResult.val != -1:
                return rightResult

            return TreeNode(-1)

        return dfs(root, p, q)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)

    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)

    s = Solution()
    print(s.lowestCommonAncestorBinaryTree(root, TreeNode(6), TreeNode(2)))