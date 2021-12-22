from nodeDepths import BinaryTreeNode

class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height

def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)

    leftChildInfo = getTreeInfo(tree.left)
    rightChildInfo = getTreeInfo(tree.right)

    longestPathThroughRoot = leftChildInfo.height + rightChildInfo.height 
    maxDiameterSoFar = max(leftChildInfo.diameter, rightChildInfo.diameter)
    currentDiameter = max(longestPathThroughRoot, maxDiameterSoFar)
    currentHeight = 1 + max(leftChildInfo.height, rightChildInfo.height)

    return TreeInfo(currentDiameter, currentHeight)

    

if __name__ == '__main__':
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(3)

    node1.left = node3
    node1.right = node2

    node4 = BinaryTreeNode(4)
    node5 = BinaryTreeNode(5)
    node6 = BinaryTreeNode(6)
    node7 = BinaryTreeNode(7)
    node3.left = node7
    node3.right = node4

    node8 = BinaryTreeNode(8)
    node9 = BinaryTreeNode(9)
    node7.left = node8
    node8.left = node9

    node4.right = node5
    node6.right = node6

    print(binaryTreeDiameter(node1))
