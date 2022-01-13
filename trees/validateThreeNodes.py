from nodeDepths import BinaryTreeNode


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    if isDescendant(nodeTwo, nodeOne):
        return isDescendant(nodeThree, nodeTwo)

    if isDescendant(nodeTwo, nodeThree):
        return isDescendant(nodeOne, nodeThree)

    return False


def isDescendant(node, target):
    while node is not None and node is not target:
        node = node.left if target.value < node.value else node.right

    return node is target


if __name__ == '__main__':
    node5 = BinaryTreeNode(5)
    node2 = BinaryTreeNode(2)
    node7 = BinaryTreeNode(7)
    node1 = BinaryTreeNode(1)
    node4 = BinaryTreeNode(4)
    node6 = BinaryTreeNode(6)
    node8 = BinaryTreeNode(8)
    node0 = BinaryTreeNode(0)
    node3 = BinaryTreeNode(3)

    node5.left = node2 
    node5.right = node7 
    
    node2.left = node1 
    node2.right = node4

    node7.left = node6
    node7.right = node8 

    node1.left = node0 

    node4.left = node3

    print(validateThreeNodes(node5, node2, node3)) #True