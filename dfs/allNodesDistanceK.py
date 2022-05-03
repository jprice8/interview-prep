import collections
from TreeNode import TreeNode


class Solution:
    def distanceK(self, root, target, K):
        def convert_into_graph(node, parent, graph):
            if not node:
                return

            if parent:
                graph[node].append(parent)

            if node.right:
                graph[node].append(node.right)
                convert_into_graph(node.right, node, graph)

            if node.left:
                graph[node].append(node.left)
                convert_into_graph(node.left, node, graph)

        graph = collections.defaultdict(list)
        visited, q, res = set(), collections.deque(), []
        convert_into_graph(root, None, graph)

        q.append((target, 0))

        while q:
            node, distance = q.popleft()
            visited.add(node)

            if distance == K:
                res.append(node.val)

            # children
            for neighbor in graph[node]:
                if neighbor not in visited:
                    q.append((neighbor, distance + 1))

        return res






if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)

    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)

    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    s = Solution()
    print(s.distanceK(root, root.left, 2)) # [7, 4, 1]