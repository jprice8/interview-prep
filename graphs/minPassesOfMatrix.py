# O(w * h) time | O(w * h) space
def minimumPassesOfMatrix(matrix):
    passes = convertNegatives(matrix)
    return passes - 1 if not containsNegative(matrix) else -1


def convertNegatives(matrix):
    queue = getAllPositiveNumbers(matrix)

    passes = 0

    while len(queue) > 0:
        currentSize = len(queue)

        while currentSize > 0:  
            currentNode = queue.pop(0)
            row, col = currentNode

            # Traverse through neighbors
            neighbors = getNeighbors(matrix, row, col)
            for neighbor in neighbors:
                row, col = neighbor
                if matrix[row][col] < 0:
                    matrix[row][col] *= -1
                    queue.append([row, col])

            currentSize -= 1

        passes += 1

    return passes


def getNeighbors(matrix, row, col):
    neighbors = []
    if row > 0:
        neighbors.append([row - 1, col]) # up
    if row < len(matrix) - 1:
        neighbors.append([row + 1, col]) # down
    if col > 0:
        neighbors.append([row, col - 1]) # left
    if col < len(matrix[row]) - 1:
        neighbors.append(row, col + 1)
    return neighbors


def getAllPositiveNumbers(matrix):
    queue = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            currentPosition = [row, col]
            if matrix[row][col] > 0:
                queue.append(currentPosition)

    return queue


def containsNegative(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] < 0:
                return True

    return False


if __name__ == "__main__":
    matrix = [
        [0, -1, -3, 2, 0],
        [1, -2, -5, -1, -3],
        [3, 0, 0, -4, -1],
    ]
    print(minimumPassesOfMatrix(matrix)) # 3