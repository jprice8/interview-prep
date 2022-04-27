import collections
from typing import List, Optional
from TreeNode import TreeNode


class Solution:
    def traverse(self, node, dct, lower = float('-inf'), upper = float('inf')):
        if not node:
            return True 
        val = node.val 
        if not(lower < val < upper):
            return False 

        if not node.left and not node.right:
            if val in dct:
                node.left = dct[val].left 
                node.right = dct[val].right 
                del dct[val]
        return self.traverse(node.left, dct, lower, val) and self.traverse(node.right, dct, val, upper)

    def can_merge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        val_cnt, root_dct = collections.defaultdict(int), {}
        for tree in trees:
            root_dct[tree.val] = tree 
            val_cnt[tree.val] += 1
            for child in (tree.left, tree.right):
                if child:
                    val_cnt[child.val] += 1

        for tree in trees:
            if val_cnt[tree.val] == 1:
                if self.traverse(tree, root_dct) and len(root_dct) <= 1:
                    return tree 
                else:
                    return None 
        return None

if __name__ == '__main__':
    t1 = TreeNode(2)
    t1.left = TreeNode(1)

    t2 = TreeNode(3)
    t2.left = TreeNode(2)
    t2.right = TreeNode(5)

    t3 = TreeNode(5)
    t3.left = TreeNode(4)

    trees = [t1, t2, t3]

    s = Solution()
    print(s.can_merge(trees))