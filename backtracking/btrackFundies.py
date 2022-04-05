class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def ternaryTreePaths(self, root):
        def dfs(node, path, res):
            # exit condition (base case), reached leaf node, append paths to result
            if all(child is None for child in node.children):
                res.append('->'.join(path) + '->' + str(node.val))
                return 

            # dfs on each non-null child
            for child in node.children:
                if child is not None:
                    dfs(child, path + [str(node.val)], res)
        res = []
        if root: dfs(root, [], res)
        return res

    def ternaryPaths2(self, root):
        def dfs(node, path, res):
            if all(child is None for child in node.children):
                res.append('->'.join(path) + '->' + str(node.val))
                return 

            for child in node.children:
                if child is not None:
                    path.append(str(node.val))
                    dfs(child, path, res)
                    path.pop()

        res = []
        if root: dfs(root, [], res)
        return res


if __name__ == '__main__':
    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node6 = Node(6)

    root.children.extend([node2, node4, node6])

    node2.children.append(node3)

    s = Solution()
    print(s.ternaryPaths2(root))