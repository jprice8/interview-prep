from typing import Optional
from TreeNode import TreeNode


class Solution:
    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base cases
        if not p and not q:
            return True
        if not p or not q:
            return False

        # preorder visit
        if p.val != q.val:
            return False

        # recursive call
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)

if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(4)
    q.right = TreeNode(3)

    s = Solution()
    print(s.sameTree(p, q))