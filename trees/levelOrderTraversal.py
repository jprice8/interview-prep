from nodeDepths import BinaryTreeNode
from collections import deque


def levelOrderTraversal(root):
    queue = deque([root])
    result = []
    while len(queue) > 0:
        n = len(queue) # Number of nodes in current level
        new_level = []
        for _ in range(n):
            node = queue.popleft()
            new_level.append(node)
            for child in [node.left, node.right]:
                if child is not None:
                    queue.append(child)
        
        result.append(new_level)

    return result


if __name__ == '__main__':
    root = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(3)
    node4 = BinaryTreeNode(4)
    node5 = BinaryTreeNode(5)
    node6 = BinaryTreeNode(6)
    node7 = BinaryTreeNode(7)

    root.left = node2 
    root.right = node3 

    node2.left = node4 
    node2.right = node5 

    node3.right = node6 

    node4.right = node7
    print(levelOrderTraversal(root))