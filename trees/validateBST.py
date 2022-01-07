from nodeDepths import BinaryTreeNode


def validateBst(root):
    isValid = True 
    traverseBst(root, isValid)
    return isValid


def traverseBst(node, isValid):
    if node is None:
        return 

    traverseBst(node.left, isValid)
    if not confirmNodeIsBst(node):
        isValid = False
    traverseBst(node.right, isValid)


def confirmNodeIsBst(node):
    # If valid BST return True
    if node.left and node.value < node.left.value:
        return False
    if node.right and node.value > node.right.value:
        return False 

    return True

if __name__ == '__main__':
    # node1 = BinaryTreeNode(1)
    # node10 = BinaryTreeNode(10)
    # nodeA5 = BinaryTreeNode(5)
    # node15 = BinaryTreeNode(15)
    # node2 = BinaryTreeNode(2)
    # nodeB5 = BinaryTreeNode(5)
    # node13 = BinaryTreeNode(13)
    # node22 = BinaryTreeNode(22)
    # node14 = BinaryTreeNode(14)

    # node10.left = nodeA5
    # node10.right = node15

    # nodeA5.left = node2 
    # nodeA5.right = nodeB5

    # node2.left = node1

    # node15.left = node13 
    # node15.right = node22 
    
    # node13.right = node14

    # print(validateBst(node10))

    node10 = BinaryTreeNode(10)
    node5 = BinaryTreeNode(5)
    node15 = BinaryTreeNode(15)
    node10b = BinaryTreeNode(10)

    node10.left = node5 
    node10.right = node15
    
    node5.right = node10b

    print(validateBst(node10))


