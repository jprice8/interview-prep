
# O((v + e) * log(v)) time | o(v) space - where v is the 
# number of vertices and e is the number of edges in the graph.
# We are using a heap here, which is optimal over a graph in this case.
def dijkstrasAlgorithm(start, edges):
    numberOfVertices = len(edges)

    minDistances = [float("inf") for _ in range(numberOfVertices)]
    minDistances[start] = 0

    minDistancesHeap = MinHeap()


class MinHeap:
    def __init__(self, array):
        # Holds the position in the heap that each vertex is at
        self.vertexMap = {idx: idx for idx in range(len(array))}
        self.heap = self.buildHeap(array)

    def isEmpty(self):
        return len(self.heap) == 0

    # O(n) time | O(1) space
    def buildHeap(self, array):
        pass

if __name__ == '__main__':
    graph = []
    print(dijkstrasAlgorithm(graph))