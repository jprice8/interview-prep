class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        """
        Perform DFS traversal on graph.

        Explore each branch as deep as you can before moving to next one.
        """
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array


node = Node('A')
node.addChild('B').addChild('C').addChild('D')
node.children[0].addChild('E').addChild('F')
node.children[2].addChild('G').addChild('H')

print(node.depthFirstSearch([]))
