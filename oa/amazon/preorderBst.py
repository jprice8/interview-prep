import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)

class Solution:
    def preorderBst(self, preorder: List[int]) -> Optional[TreeNode]:
        def dfs(lower = float('-inf'), upper = float('inf')):
            nonlocal idx
            if idx == n:
                return None 

            val = preorder[idx]
            if val < lower or val > upper:
                return None 

            idx += 1
            root = TreeNode(val)
            root.left = dfs(lower, val)
            root.right = dfs(val, upper)
            return root 

        idx = 0
        n = len(preorder)
        return dfs()
            



if __name__ == '__main__':
    s = Solution()
    print(s.preorderBst([8, 5, 1, 7, 10, 12]))