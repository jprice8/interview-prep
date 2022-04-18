from typing import List, Optional
from TreeNode import TreeNode


class Solution:
    def construction(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.construction(preorder[1:mid + 1], inorder[:mid])
        root.right = self.construction(preorder[mid + 1:], inorder[mid + 1:])
        return root



if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    s = Solution()
    print(s.construction(preorder, inorder))