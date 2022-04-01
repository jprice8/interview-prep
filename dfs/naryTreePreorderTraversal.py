from typing import List
from TreeNode import TreeNode


class Solution:
    def preorderRecursive(self, root: TreeNode) -> List[int]:
        result = []
        def dfs(node, result):
            if node is None:
                return 

            # Preorder visit
            result.append(node.val)

            for child in node.children:
                if child is not None:
                    dfs(node.child, result)

        dfs(root, result)
        return result

    def preorderIterative(self, root: TreeNode) -> List[int]:
        if root is None:
            return None

        stack, result = [root], []
        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(node.children)

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.example())