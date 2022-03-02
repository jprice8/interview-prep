class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None 
        self.right = None

    def __repr__(self) -> str:
        return str(self.val)


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """
        Enocdes a tree to a single string.
        """
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str) -> TreeNode:
        """
        Decodes your encoded data to tree.
        """
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None 

            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node 
        return dfs()


class Solution2:
    def serialize(self, root):
        result = []
        def dfs(node):
            if node is None:
                result.append('N')
                return 

            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ''.join(result)


    def deserialize(self, data):
        nodeList = data.split(',')
        self.i = 0
        def dfs():
            if nodeList[self.i] == 'N':
                self.i += 1
                return None 

            node = TreeNode(nodeList[self.i])
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()



if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node1.left = node2 
    node1.right = node3 
    node3.left = node4 
    node3.right = node5

    ser = Codec()
    deser = Codec()
    # print(deser.deserialize(ser.serialize(node1)))

    ser = Solution2()
    deser = Solution2()
    print(deser.deserialize(ser.serialize(node1)))