import collections
from nodeDepths import BinaryTreeNode


def invertBinaryTree(tree):
    if tree is None:
        return 

    leftChild = tree.left
    rightChild = tree.right

    tree.left = rightChild
    tree.right = leftChild

    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

class Solution:
    def invertTree(self, root):
        q = collections.deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node is None:
                break

            for child in [node.right, node.left]:
                q.append(child)

            tmpLeft = node.left
            node.left = node.right
            node.right = tmpLeft

        return root


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None 


if __name__ == '__main__':
    node1 = BinaryTreeNode(1)
    node2 = BinaryTreeNode(2)
    node3 = BinaryTreeNode(3)

    node1.left = node2 
    node1.right = node3

    node4 = BinaryTreeNode(4)
    node5 = BinaryTreeNode(5)
    node6 = BinaryTreeNode(6)
    node2.left = node4
    node2.right = node5

    node7 = BinaryTreeNode(7)
    node8 = BinaryTreeNode(8)
    node9 = BinaryTreeNode(9)
    node3.left = node6
    node3.right = node7 

    node4.left = node8 
    node4.right = node9

    # print(invertBinaryTree(node1))
    s = Solution()
    print(s.invertTree(node1))