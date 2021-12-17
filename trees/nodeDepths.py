class BinaryTreeNode:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 

    def __repr__(self) -> str:
        return str(self.value)


def preorder(node):
    """
    Visit root, left, then right children.
    """
    if node:
        print(node.value)
        preorder(node.left)
        preorder(node.right)

# O(n) time where n is the number of nodes in the tree | O(h) space where h is the height of the tree
def recursiveNodeDepths(node, depth = 0):
    if node is None:
        return 0

    return depth + recursiveNodeDepths(node.left, depth + 1) + recursiveNodeDepths(node.right, depth + 1)

# O(n) time | O(h) space where h is the height of the tree
def iterativeNodeDepths(node):
    sumOfDepths = 0
    stack = [{'node': node, 'depth': 0}]

    while len(stack) > 0:
        currNode = stack.pop()
        node, depth = currNode['node'], currNode['depth']

        if node is None:
            continue

        sumOfDepths += depth 
        stack.append({'node': node.left, 'depth': depth + 1})
        stack.append({'node': node.right, 'depth': depth + 1})

    return sumOfDepths



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
    print(recursiveNodeDepths(node1))