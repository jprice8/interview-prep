from nodeDepths import BinaryTreeNode

# O(n) time | O(n) space - where n represents nodes in the tree
# We can improve space by using recursion instead of auxillary data structure
def flattenBinaryTree(root):
     nodes = []
     inOrderTraverse(root, nodes)
     left = handleFlatten(nodes)
     return left


def inOrderTraverse(tree, nodes):
    if tree is None:
        return
    inOrderTraverse(tree.left, nodes)
    nodes.append(tree)
    inOrderTraverse(tree.right, nodes)


def handleFlatten(nodes):
    # Edge cases
    if len(nodes) == 0:
        return []
    elif len(nodes) == 1:
        return nodes[0]
    else:
        # Set first and last node
        nodes[0].left = None 
        nodes[0].right = nodes[1]
        nodes[-1].left = nodes[-2] 
        nodes[-1].right = None 
        for i in range(1, len(nodes) - 1):
            nodes[i].left = nodes[i - 1]
            nodes[i].right = nodes[i + 1]

    return nodes[0]


def flattenBinaryTreeOptimal(root):
    pass


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
    node8 = BinaryTreeNode(8)
    node5.left = node7 
    node5.right = node8 
    node3.left = node6

    print(flattenBinaryTree(node1))