import queue
from glossary import Node


class Solution(Node):
    # O(V+E) time | O(V) space - where v are the vertices and e are 
    # the edges of the graph.
    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array


if __name__ == '__main__':
    graph = Solution('A')
    graph.addChild('B').addChild('C').addChild('D')
    graph.children[0].addChild('E').addChild('F')
    graph.children[2].addChild('G').addChild('H')
    graph.children[0].children[1].addChild('I').addChild('J')
    graph.children[2].children[0].addChild('K')
    print(graph.breadthFirstSearch([])) # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']