from nodeDepths import BinaryTreeNode


# O(n) time | O(d) space - where d is the depth of the tree
def rightSiblingTree(root):
    mutate(root, None, None)
    return root 


def mutate(node, parent, isLeftChild):
    if node is None:
        return 

    left, right = node.left, node.right 
    mutate(left, node, True)
    if parent is None:
        node.right = None 
    elif isLeftChild:
        node.right = parent.right
    else:
        if parent.right is None:
            node.right = None 
        else:
            node.right = parent.right.left 
    mutate(right, node, False)


if __name__ == '__main__':
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(3)
    node4 = BinaryTreeNode(4)
    node5 = BinaryTreeNode(5)
    node6 = BinaryTreeNode(6)
    node7 = BinaryTreeNode(7)
    node8 = BinaryTreeNode(8)
    node9 = BinaryTreeNode(9)
    node10 = BinaryTreeNode(10)
    node11 = BinaryTreeNode(11)
    node12 = BinaryTreeNode(12)
    node13 = BinaryTreeNode(13)
    node14 = BinaryTreeNode(14)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    node3.left = node6
    node3.right = node7

    node4.left = node8
    node4.right = node9

    node5.right = node10 

    node6.left = node11 

    node7.left = node12 
    node7.right = node13 

    node11.left = node14

    print(rightSiblingTree(node1))