from binaryTreeWithParent import BinaryTree
# TODO: Try and solve iterative preorder and postorder traversal

def iterativeInOrderTraversal(tree, callback):
    currentNode = tree
    previousNode = None
    while currentNode is not None:
        if previousNode is None or previousNode == currentNode.parent:
            if currentNode.left is not None:
                nextNode = currentNode.left
            else:
                callback(currentNode)
                nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        elif previousNode == currentNode.left:
            callback(currentNode)
            nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        else:
            nextNode = currentNode.parent
        previousNode = currentNode
        currentNode = nextNode


def callback(value):
    print(value)


if __name__ == '__main__':
    node1 = BinaryTree(1)
    node2 = BinaryTree(2)
    node3 = BinaryTree(3)
    node1.left = node2
    node2.parent = node1
    node1.right = node3
    node3.parent = node1

    node4 = BinaryTree(4)
    node5 = BinaryTree(5)
    node2.left = node4
    node4.parent = node2

    node6 = BinaryTree(6)
    node7 = BinaryTree(7)
    node8 = BinaryTree(8)
    node9 = BinaryTree(9)
    node4.right = node9
    node9.parent = node4
    node3.left = node6
    node6.parent = node3
    node3.right = node7
    node7.parent = node3

    print(iterativeInOrderTraversal(node1, callback))
