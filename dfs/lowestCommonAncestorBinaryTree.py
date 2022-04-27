from TreeNode import TreeNode


class Solution:
    def iterative(self, root, p, q):
        stack = [root]

        parent = {root: None}

        # Iter until we find both p and q
        while p not in parent or q not in parent:
            node = stack.pop()

            if node.left:
                parent[node.left] = node 
                stack.append(node.left)
            if node.right:
                parent[node.right] = node 
                stack.append(node.right)

        # Ancestors set for node p
        ancestors = set()

        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears
        # in p's ancestor set() is their LCA.
        while q not in ancestors:
            q = parent[q]
        return q


    def lca(self, root, p, q):
        def dfs(node, p, q):
            # base case
            if node is None:
                return
            
            # preorder visit
            if node.val == p or node.val == q:
                return node

            # recursive calls
            leftResult = dfs(node.left, p, q)
            rightResult = dfs(node.right, p, q)

            # postorder visit
            # checking to see if p or q is value
            # check to see if our children have seen p or q
            if leftResult and rightResult:
                return node
            
            if leftResult:
                return leftResult
            if rightResult:
                return rightResult
        
        return dfs(root, p, q)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)

    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)

    s = Solution()
    # print(s.lowestCommonAncestorBinaryTree(root, TreeNode(6), TreeNode(2)))
    # print(s.lca(root, TreeNode(6), TreeNode(2)))
    print(s.iterative(root, TreeNode(6), TreeNode(2)))