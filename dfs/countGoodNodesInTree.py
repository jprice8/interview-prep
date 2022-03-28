from TreeNode import TreeNode


class Solution:
    def countGoodNodes(self, root):
        def dfs(node, maxParent):
            if node is None:
                return 0

            newParent = max(maxParent, node.val)
            leftGoodNodes = dfs(node.left, newParent)
            rightGoodNodes = dfs(node.right, newParent)

            # Postorder visit
            return leftGoodNodes + rightGoodNodes + (node.val >= maxParent)

        return dfs(root, root.val)

    def countGoodNodesIter(self, root):
        stack = [(root, root.val)]
        goodNodes = 0
        while stack:
            node, maxParent = stack.pop()
            if node is not None:
                if node.val >= maxParent:
                    goodNodes += 1
                if node.left:
                    stack.append((node.left, max(maxParent, node.val)))
                if node.right:
                    stack.append((node.right, max(maxParent, node.val)))

        return goodNodes


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(6)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(8)

    s = Solution()
    print(s.countGoodNodesIter(root)) # 3
