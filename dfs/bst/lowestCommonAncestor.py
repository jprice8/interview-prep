from TreeNode import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, p, q):
            if node is None:
                return 
            
            if p.val < node.val and q.val < node.val:
                return dfs(node.left, p, q)
            elif p.val > node.val and q.val > node.val:
                return dfs(node.right, p, q)
            else:
                return node
            
        return dfs(root, p, q)


if __name__ == '__main__':
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)

    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)

    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    s = Solution()
    print(s.lowestCommonAncestor(root, TreeNode(2), TreeNode(4)))