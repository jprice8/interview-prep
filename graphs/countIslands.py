# def countIslands(matrix):
#     nonIslandOnes = [[False for value in row] for row in matrix]
#     islandsSeen = 0
#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#             if matrix[row][col] == 1:
#                 # Traverse graph if cell is land
#                 traverseGraph(row, col, matrix, nonIslandOnes, islandsSeen)

#     # Iterate through matrix and check against nonIslandOnes...
#     # for row in range(len(matrix)):
#         # for col in range(len(matrix[row])):
#             # Logic here

#     return islandsSeen

# def traverseGraph(row, col, matrix, nonIslandOnes, islandsSeen):
#     # DFS
#     stack = [[row, col]]
#     while len(stack) > 0:
#         currentNode = stack.pop()
#         currentRow, currentCol = currentNode

#         # Check if already visited land
#         alreadyVisited = nonIslandOnes[currentRow][currentCol]
#         if alreadyVisited:
#             continue 
#         # Mark visited
#         nonIslandOnes[currentRow][currentCol] = True 

#         # Add nodes to visit to stack
#         nodesToVisit = getNodesToVisit(currentRow, currentCol, matrix)
#         for node in nodesToVisit:
#             stack.append(node)
#     islandsSeen += 1


# def getNodesToVisit(row, col, matrix):
#     nodesToVisit = []
#     if row - 1 >= 0: # UP
#         nodesToVisit.append([row - 1, col])
#     if row + 1 <= len(matrix) - 1: # DOWN
#         nodesToVisit.append([row + 1, col])
#     if col - 1 >= 0: # LEFT
#         nodesToVisit.append([row, col - 1])
#     if col + 1 <= len(matrix[row]) - 1: # RIGHT
#         nodesToVisit.append([row, col + 1])
#     return nodesToVisit


def countIslands(matrix):
    visited = [[False for _ in row] for row in matrix]
    islandsSeen = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if explore(row, col, matrix, visited):
                islandsSeen += 1

    return islandsSeen

def explore(row, col, matrix, visited):
    rowInBounds = 0 < row and row < len(matrix) - 1
    colInBounds = 0 < col and col < len(matrix[0]) - 1
    # Check in matrix
    if not rowInBounds or not colInBounds: 
        return False 
    # Check for land
    if matrix[row][col] == 0: 
        return False

    # Check if already visited
    alreadyVisited = visited[row][col]
    if alreadyVisited:
        return False

    visited[row][col] = True

    explore(row - 1, col, matrix, visited) # Traverse up
    explore(row + 1, col, matrix, visited) # Traverse down
    explore(row, col - 1, matrix, visited) # Traverse left
    explore(row, col + 1, matrix, visited) # Traverse right

    return True

if __name__ == '__main__':
    matrix = [
        [1, 0, 0, 0],
        [1, 0, 1, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
    ]

    print(countIslands(matrix))