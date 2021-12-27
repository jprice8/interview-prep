from nodeDepths import BinaryTreeNode

class TreeInfo:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height


def isBalanced(tree):
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(True, -1)

    leftChildInfo = getTreeInfo(tree.left)
    rightChildInfo = getTreeInfo(tree.right)

    subtreeHeightDifference = abs(leftChildInfo.height - rightChildInfo.height)

    isBalanced = (
        leftChildInfo.isBalanced and rightChildInfo.isBalanced and abs(leftChildInfo.height - rightChildInfo.height) <= 1
    )
    height = max(leftChildInfo.height, rightChildInfo.height) + 1
    return TreeInfo(isBalanced, height)



if __name__ == '__main__':
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(3)
    node4 = BinaryTreeNode(4)
    node5 = BinaryTreeNode(5)
    node6 = BinaryTreeNode(6)
    node7 = BinaryTreeNode(7)
    node8 = BinaryTreeNode(8)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    node3.right = node6

    node5.left = node7 
    node5.right = node8


    # print(iterativeNodeDepths(node1))
    print(isBalanced(node1))