from typing import Optional
from nodeDepths import BinaryTreeNode


class Solution:
    def subtreeOfAnother(self, root: Optional[BinaryTreeNode], subRoot: Optional[BinaryTreeNode]) -> bool:
        if not subRoot: return True 
        if not root: return False 

        if self.sameTree(root, subRoot):
            return True 
        return (self.subtreeOfAnother(root.left, subRoot) or 
                self.subtreeOfAnother(root.right, subRoot))

    def sameTree(self, p, q):
        if not p and not q:
            return True 
        if p and q and p.value == q.value:
            return (self.sameTree(p.left, q.left) and 
                self.sameTree(p.right, q.right))

        return False


if __name__ == '__main__':
    root = BinaryTreeNode(3)
    root.left = BinaryTreeNode(4)
    root.right = BinaryTreeNode(5)

    root.left.left = BinaryTreeNode(1)
    root.left.right = BinaryTreeNode(2)

    subRoot = BinaryTreeNode(4)
    subRoot.left = BinaryTreeNode(1)
    subRoot.right = BinaryTreeNode(2)

    s = Solution()
    print(s.subtreeOfAnother(root, subRoot))
