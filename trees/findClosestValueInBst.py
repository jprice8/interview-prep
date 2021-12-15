import unittest
from typing import List


def findClosestValueInBst(tree, target):
    pass

# def inOrderTraversal(root) -> List[int]:
#     """
#     Traverse the tree given the root.
#     """
#     res = []
#     if root:
#         # Traverse the left branch first
#         res = inOrderTraversal(root.left)
#         # Append value to result array
#         res.append(root.value)
#         # Traverse right branch next
#         res = res + inOrderTraversal(root.right)

#     return res


class BST:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        expected = 13
        actual = findClosestValueInBst(root, 12)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()