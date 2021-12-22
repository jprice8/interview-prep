from binaryTreeWithParent import BinaryTree


def findSuccessor(tree, target):
    inOrderNodes = getInOrderTraversal(tree)
    lastNode = None
    currentNode = None
    while len(inOrderNodes) > 0:
        currentNode = inOrderNodes.pop()

        if currentNode.value == target:
            return lastNode.value

        lastNode = currentNode


    return None


def getInOrderTraversal(node, order=[]):
    if node is None:
        return order 

    getInOrderTraversal(node.left, order)
    order.append(node)
    getInOrderTraversal(node.right, order)

    return order


node1 = BinaryTree(1)
node2 = BinaryTree(2)
node3 = BinaryTree(3)

node1.left = node2
node2.parent = node1
node1.right = node3
node3.parent = node1

node4 = BinaryTree(4)
node5 = BinaryTree(5)
node6 = BinaryTree(6)
node2.left = node4
node4.parent = node2
node2.right = node5
node5.parent = node2
node4.left = node6
node6.parent = node4

print(findSuccessor(node1, 2))