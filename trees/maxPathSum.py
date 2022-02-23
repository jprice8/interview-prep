from nodeDepths import BinaryTreeNode


def maxPathSum(tree):
    _, maxPathSum = findMaxSum(tree)
    return maxPathSum

def findMaxSum(tree):
    if tree is None:
        return (0, 0)

    leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
    rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

    value = tree.value
    maxSumAsBranch = max(maxChildSumAsBranch + value, value)
    maxSumAsRootNode = max(leftMaxSumAsBranch + value + rightMaxSumAsBranch, maxSumAsBranch)
    maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)

    return (maxSumAsBranch, maxPathSum)


class Solution:
    def maxPathSum(self, root: BinaryTreeNode) -> int:
        res = [root.value]

        def dfs(root):
            nonlocal res
            if root is None:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            # Values could be negative so update
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            # 1) Compute max path sum WITH split
            res[0] = max(res[0], root.value + leftMax + rightMax)
            # 2) Compute max path sum WITHOUT split
            return root.value + max(leftMax, rightMax)

        dfs(root)
        return res[0]



if __name__ == '__main__':
    # node1 = BinaryTreeNode(1)
    # node2 = BinaryTreeNode(2)
    # node3 = BinaryTreeNode(3)
    # node1.left = node2
    # node1.right = node3

    # node4 = BinaryTreeNode(4)
    # node5 = BinaryTreeNode(5)
    # node2.left = node4 
    # node2.right = node5

    # node6 = BinaryTreeNode(6)
    # node7 = BinaryTreeNode(7)
    # node3.left = node6
    # node3.right = node7

    node10 = BinaryTreeNode(10)
    nodeN5 = BinaryTreeNode(-5)
    node20 = BinaryTreeNode(20)
    node15 = BinaryTreeNode(15)
    node7 = BinaryTreeNode(7)

    node10.left = nodeN5 
    node10.right = node20 

    node20.left = node15 
    node20.right = node7


    # print(maxPathSum(node1))
    s = Solution()
    print(s.maxPathSum(node10))