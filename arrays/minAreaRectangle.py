def minAreaRectangle(points):
    xPairs = []
    yPairs = []
    rectangles = []

    # Loop through all points
    for i in range(len(points)):
        currentPoint = points[i] 

        # Loop through other points
        for j in range(len(points)):
            # Go through points but the one we are currently on.
            if i != j:
                checkPoint = points[j]

                # Check to see if x matches
                if currentPoint[0] == checkPoint[0]:
                    xPairs.append([currentPoint, checkPoint])

                # Check to see if y matches
                elif currentPoint[1] == checkPoint[1]:
                    yPairs.append([currentPoint, checkPoint])

    # If no matches return early
    if not xPairs or not yPairs:
        return 0

    # Find matching yPairs with same respective x coordinates.
    for i in range(len(yPairs)):
        currentY = yPairs[i]
        for j in range(len(yPairs)):
            if i != j:
                checkY = yPairs[j]
                # If matching x coordinates, add to rectangles list.
                if currentY[0][0] == checkY[0][0] and currentY[1][0] == checkY[1][0]:
                    rectangles.append([currentY, checkY])


    minHeight = 0
    for rectangle in rectangles:
        x1 = rectangle[0][0]
        x2 = rectangle[1][0]
        y1 = rectangle[0][1]
        y2 = rectangle[1][1]
        area = calculateArea(x1, x2, y1, y2)
        if area < minHeight:
            minHeight = area

    return minHeight


def calculateArea(x1, x2, y1, y2):
    width = x1 - x2 
    height = y1 - y2 
    return width * height


#### AE Solution 1 ####
# O(n^2) time | O(n) space - where n is the length of points
def minimumAreaRectangle1(points):
    columns = initializeColumns(points)
    minimumAreaFound = float("inf")
    edgesParallelToYAxis = {}

    sortedColumns = sorted(columns.keys())
    for x in sortedColumns:
        yValuesInCurrentColumn = columns[x]
        yValuesInCurrentColumn.sort()

        for currentIdx, y2 in enumerate(yValuesInCurrentColumn):
            for previousIdx in range(currentIdx):
                y1 = yValuesInCurrentColumn[previousIdx]
                pointString = str(y1) + ":" + str(y2)

                if pointString in edgesParallelToYAxis:
                    currentArea = (x - edgesParallelToYAxis[pointString]) * (y2 - y1)
                    minimumAreaFound = min(minimumAreaFound, currentArea)

                edgesParallelToYAxis[pointString] = x 

    return minimumAreaFound if minimumAreaFound != float("inf") else 0


def initializeColumns(points):
    columns = {}

    for point in points:
        x, y = point 
        if x not in columns:
            columns[x] = []
        
        columns[x].append(y)

    return columns


if __name__ == '__main__':
    points = [
        [1, 5],
        [5, 1],
        [4, 2],
        [2, 4],
        [2, 2],
        [1, 2],
        [4, 5],
        [2, 5],
        [-1, -2],
    ]
    print(minimumAreaRectangle1(points))