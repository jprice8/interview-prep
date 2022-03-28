from typing import Optional
from nodeDepths import BinaryTreeNode


class Solution:
    def sameTree(self, p: Optional[BinaryTreeNode], q: Optional[BinaryTreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.value != q.value:
            return False

        return (self.sameTree(p.left, q.left) and 
                self.sameTree(p.right, q.right))


if __name__ == '__main__':
    p = BinaryTreeNode(1)
    p.left = BinaryTreeNode(2)
    p.right = BinaryTreeNode(3)

    q = BinaryTreeNode(1)
    q.left = BinaryTreeNode(2)
    q.right = BinaryTreeNode(3)

    s = Solution()
    print(s.sameTree(p, q))
