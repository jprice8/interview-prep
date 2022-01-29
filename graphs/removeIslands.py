def removeIslands(matrix):
    onesConnectedToBorder = [[False for value in row] for row in matrix] 
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            rowIsBorder = row == 0 or row == len(matrix) - 1
            colIsBorder = col == 0 or col == len(matrix[col]) - 1
            isBorder = rowIsBorder or colIsBorder

            if not isBorder:
                continue 

            findOnesConnectedToBorder(matrix, row, col, onesConnectedToBorder)

    # Set 0 to all that's not connected to border
    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[row]) - 1):
            if onesConnectedToBorder[row][col]:
                continue 

            matrix[row][col] = 0

    return matrix


def findOnesConnectedToBorder(matrix, row, col, onesConnectedToBorder):
    nodesToExplore = [[row, col]]
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        currentRow, currentCol = currentNode
        alreadyVisited = onesConnectedToBorder[currentRow][currentCol]
        # Pass over if already visited
        if alreadyVisited:
            continue

        onesConnectedToBorder[currentRow][currentCol] = True

        neighbors = getNeighbors(matrix, row, col)
        
        # Add children to stack
        for neighbor in neighbors:
            row, col = neighbor

            if matrix[row][col] != 1:
                continue 

            nodesToExplore.append(neighbor)


def getNeighbors(matrix, row, col):
    neighbors = []
    if row - 1 >= 0: # up
        neighbors.append((row - 1, col))
    if row + 1 < len(matrix): # down
        neighbors.append((row + 1, col))
    if col - 1 >= 0: # left
        neighbors.append((row, col - 1))
    if col + 1 < len(matrix[row]): # right
        neighbors.append((row, col + 1))
    return neighbors

    

def traverseNode(i, j, matrix, visited, islandBoys):
    nodesToExplore = [[i, j]]
    while len(nodesToExplore):
        # Poop node off stack for current
        currentNode = nodesToExplore.pop()
        # Logic goes here
        i = currentNode[0]
        j = currentNode[1]

        if visited[i][j]:
            continue 
        visited[i][j] = True 
        # If not an islandBoy
        if matrix[i][j] == 0:
            continue 

        islandBoys += 1

        # Add children to stack


def removeIslandsAE(matrix):
    onesConnectedToBorder = [[False for value in row] for row in matrix]

    # Find all the 1s that are not islands
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            rowIsBorder = row == 0 or row == len(matrix) - 1
            colIsBorder = col == 0 or col == len(matrix[row]) - 1
            isBorder = rowIsBorder or colIsBorder

            if not isBorder:
                continue 

            # Find ones connect to border helper

    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[row]) - 1):
            if onesConnectedToBorder[row][col]:
                continue 

            matrix[row][col] = 0

    return matrix


def removeIslandsRecursive(matrix):
    visited = [[False for _ in row] for row in matrix] 
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            rowIsBorder = row == 0 or row == len(matrix) - 1 
            colIsBorder = col == 0 or col == len(matrix[0]) - 1 
            isBorder = rowIsBorder or colIsBorder
            if not isBorder:
                continue 

            if matrix[row][col] != 1:
                continue 

            explore(row, col, matrix, visited)

    # remove islands
    for row in range(len(visited)):
        for col in range(len(visited[0])):
            currentLocation = visited[row][col]
            if currentLocation != True:
                matrix[row][col] = 0

    return matrix

def explore(row, col, matrix, visited):
    stack = [[row, col]]

    while len(stack) > 0:
        currentPosition = stack.pop()
        currentRow, currentCol = currentPosition

        alreadyVisited = visited[currentRow][currentCol]
        if alreadyVisited:
            continue 

        visited[currentRow][currentCol] = True 

        neighbors = getNeighbors(currentRow, currentCol, matrix)

        for neighbor in neighbors:
            nRow, nCol = neighbor

            if matrix[nRow][nCol] != 1:
                continue 

            stack.append(neighbor)


def getNeighbors(row, col, matrix):
    neighbors = []
    if row - 1 >= 0:
        neighbors.append([row - 1, col])
    if row + 1 < len(matrix):
        neighbors.append([row + 1, col])
    if col - 1 >= 0:
        neighbors.append([row, col - 1])
    if col + 1 < len(matrix[0]):
        neighbors.append([row, col + 1])
    return neighbors
    

if __name__ == '__main__':
    matrix = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]

    # matrix = [
        # [1, 0, 0, 0],
        # [1, 0, 1, 0],
        # [1, 0, 0, 0],
        # [1, 1, 1, 0],
    # ]
    print(removeIslandsRecursive(matrix))