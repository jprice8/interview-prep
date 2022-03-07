from nodeDepths import BinaryTreeNode

class Solution:
    def validateBst(self, root):
        def dfs(node, minNumber, maxNumber):
            if node is None:
                return True

            if node.value <= minNumber or node.value >= maxNumber:
                return False
            leftIsValid = dfs(node.left, minNumber, node.value)
            return leftIsValid and dfs(node.right, node.value, maxNumber)

        return dfs(root, float('-inf'), float('inf'))
        

if __name__ == '__main__':
    node5 = BinaryTreeNode(5)
    node4 = BinaryTreeNode(4)
    node6 = BinaryTreeNode(6)
    node3 = BinaryTreeNode(3)
    node7 = BinaryTreeNode(7)

    node5.left = node4 
    node5.right = node6 

    node6.left = node3 
    node6.right = node7

    s = Solution()
    print(s.validateBst(node5))

