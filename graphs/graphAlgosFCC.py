from glossary import Node


GRAPH = {
    'a': ['b', 'c', 'd'],
    'b': ['e', 'f'],
    'c': [],
    'd': ['g', 'h'],
    'e': [],
    'f': ['i', 'j'],
    'g': ['k'],
    'h': [],
    'i': [],
    'j': [],
    'k': []
}

hasPathGraph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': [],
}

def dfsIteratively(graph, source, array):
    stack = [source] 
    while len(stack) > 0:
        current = stack.pop()
        array.append(current)
        for child in graph[current]:
            stack.append(child)
    return array

def dfsRecursive(graph, source, array):
    array.append(source)
    for child in graph[source]:
        dfsRecursive(graph, child, array)

    return array

# BFS only possible using iteration (stack vs queue)
def bfsIteratively(graph, source, array):
    queue = [source]
    while len(queue) > 0:
        current = queue.pop(0)
        array.append(current)
        for child in graph[current]:
            queue.append(child)

    return array

# n = # nodes
# e = # edges
# Time: O(e)
# Space: O(n)
def hasPathDfsIteratively(source, destination):
    stack = [source]
    while len(stack) > 0:
        current = stack.pop()
        if current == destination:
            return True 
        for child in hasPathGraph[current]:
            stack.append(child)

    return False

def hasPathDfsRecursively(source, destination):
    if source == destination:
        return True
    for child in hasPathGraph[source]:
        if hasPathDfsRecursively(child, destination):
            return True

    return False



if __name__ == '__main__':
    #### dfs ####
    # print(dfsIteratively(GRAPH, 'a', []))
    # print(dfsRecursive(GRAPH, 'a', [])) # abefijcdgkh

    #### bfs ####
    # print(bfsIteratively(GRAPH, 'a', [])) # acbedf

    #### has path ####
    print(hasPathDfsIteratively('f', 'j')) # False
    # print(hasPathDfsRecursively('f', 'j')) # False