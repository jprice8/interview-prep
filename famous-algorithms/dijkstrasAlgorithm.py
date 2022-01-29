
# O((v + e) * log(v)) time | o(v) space - where v is the 
# number of vertices and e is the number of edges in the graph.
# We are using a heap here, which is optimal over a graph in this case.
# def dijkstrasAlgorithm(start, edges):
#     numberOfVertices = len(edges)

#     minDistances = [float("inf") for _ in range(numberOfVertices)]
#     minDistances[start] = 0

#     minDistancesHeap = MinHeap()


# class MinHeap:
#     def __init__(self, array):
#         # Holds the position in the heap that each vertex is at
#         self.vertexMap = {idx: idx for idx in range(len(array))}
#         self.heap = self.buildHeap(array)

#     def isEmpty(self):
#         return len(self.heap) == 0

#     # O(n) time | O(1) space
#     def buildHeap(self, array):
#         pass


# O(v^2 + e) time | O(v) space - where v is the number 
# of vertices and e is the number of edges in the input graph.
def dijkstrasAlgorithm1(start, edges):
    numberOfVertices = len(edges)

    minDistances = [float("inf") for _ in range(numberOfVertices)]
    minDistances[start] = 0

    visited = set()

    while len(visited) != numberOfVertices:
        vertex, currentMinDistance = getVertexWithMinDistance(minDistances, visited)

        if currentMinDistance == float("inf"):
            break 

        visited.add(vertex)

        for edge in edges[vertex]:
            destination, distanceToDestination = edge 

            if destination in visited:
                continue 

            newPathDistance = currentMinDistance + distanceToDestination
            currentDestinationDistance = minDistances[destination]
            if newPathDistance < currentDestinationDistance:
                minDistances[destination] = newPathDistance

    return list(map(lambda x: -1 if x == float("inf") else x, minDistances))


def getVertexWithMinDistance(distances, visited):
    currentMinDistance = float('inf')
    vertex = -1

    for vertexIdx, distance in enumerate(distances):
        if vertexIdx in visited:
            continue 

        if distance <= currentMinDistance:
            vertex = vertexIdx
            currentMinDistance = distance 

    return vertex, currentMinDistance


#### Dijkstra's Algorithm with Heap ####
def dijkstrasWithHeap(start, edges):
    numberOfVertices = len(edges)

    minDistances = [float("inf") for _ in range(numberOfVertices)]
    minDistances[start] = 0

    minDistancesHeap = MinHeap([(idx, float("inf")) for idx in range(numberOfVertices)])


class MinHeap:
    def __init__(self, array):
        self.vertexMap = {idx: idx for idx in range(len(array))}
        self.heap = self.buildHeap(array)

    def isEmpty(self):
        return len(self.heap) == 0

    # O(n) time | O(1) space
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            # TODO
            self.siftDown(currentIdx, len(array) - 1, array)
        return array


if __name__ == '__main__':
    start = 0
    edges = [
        [[1, 7]],
        [[2, 6], [3, 20], [4, 3]],
        [[3, 14]],
        [[4, 2]],
        [],
        [],
    ]
    # print(dijkstrasAlgorithm1(start, edges)) # [0, 7, 13, 27, 10, -1]
    print(dijkstrasWithHeap(start, edges)) # [0, 7, 13, 27, 10, -1]