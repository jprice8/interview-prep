class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def __repr__(self):
        return str(self.name)

    def addChild(self, name):
        self.children.append(Node(name))
        return self


class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None 

    def __repr__(self):
        return str(self.name)

    def addDescendants(self, *descendants):
        for descendant in descendants:
            descendant.ancestor = self
