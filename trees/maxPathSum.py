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


if __name__ == '__main__':
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(3)
    node1.left = node2
    node1.right = node3

    node4 = BinaryTreeNode(4)
    node5 = BinaryTreeNode(5)
    node2.left = node4 
    node2.right = node5

    node6 = BinaryTreeNode(6)
    node7 = BinaryTreeNode(7)
    node3.left = node6
    node3.right = node7


    print(maxPathSum(node1))