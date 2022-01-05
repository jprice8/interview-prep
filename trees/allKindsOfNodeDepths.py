from nodeDepths import BinaryTreeNode


def allKindsOfNodeDepths(root):
    if root is None:
        return 0

    return allKindsOfNodeDepths(root.left) + allKindsOfNodeDepths(root.right) + nodeDepths(root)


def nodeDepths(node, depth = 0):
    if node is None:
        return 0

    return nodeDepths(node.left, depth + 1) + nodeDepths(node.right, depth + 1) + depth


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

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    node3.left = node6
    node3.right = node7

    node4.left = node8
    node4.right = node9

    # print(iterativeNodeDepths(node1))
    print(allKindsOfNodeDepths(node1))