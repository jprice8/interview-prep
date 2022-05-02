import collections
from TreeNode import TreeNode


class Solution:
    def rightSideView(self, root):
        # 1) While queue
        # 2) Iterate through length of queue for level
        # 3) If node, add children to queue
        # 4) At the end of each level, add the last element in the queue to the result
        # 5) Return result
        if root is None:
            return []
        result = [root.val]
        q = collections.deque([])
        q.append(root)

        while q:
            q_length = len(q)
            for _ in range(q_length):
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            if len(q) > 0:
                result.append(q[-1])
        return result



if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    s = Solution()
    print(s.rightSideView(root))