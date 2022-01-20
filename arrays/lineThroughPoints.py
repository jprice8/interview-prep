def lineThroughPoints(points):
    runningMax = 2

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            # Calculate slope between i and j 
            slopeIJ = calculateSlope(points[i], points[j])
            currentMax = 2

            # Check that slope against other points
            for k in range(len(points)):
                if k == i or k == j:
                    continue
                # Calculate slope between i and k
                slopeIK = calculateSlope(points[i], points[k])
                if slopeIK == slopeIJ:
                    currentMax += 1

            runningMax = max(runningMax, currentMax)

    return runningMax


def calculateSlope(point1, point2):
    x1, y1 = point1 
    x2, y2 = point2

    if y2 == y1: return 0
    if x2 == x1: return 1

    return (y2 - y1) / (x2 - x1)


def aeSolution(points):
    maxNumberOfPointsOnLine = 1

    for idx1, p1 in enumerate(points):
        slopes = {}
        for idx2 in range(idx1 + 1, len(points)):
            p2 = points[idx2]
            rise, run = getSlopeOfLine(p1, p2)
            slopeKey = createHashableKeyForRational(rise, run)
            if slopeKey not in slopes:
                slopes[slopeKey] = 1
            
            slopes[slopeKey] += 1

        maxNumberOfPointsOnLine = max(maxNumberOfPointsOnLine, max(slopes.values(), default=0))

    return maxNumberOfPointsOnLine


def getSlopeOfLine(p1, p2):
    x1, y1 = p1 
    x2, y2 = p2 
    slope = [1, 0] # Slope of vertical line

    if x1 != x2: # If line is not vertical
        xDiff = x1 - x2 
        yDiff = y1 - y2 
        gcd = getGreatestCommonDivisor(abs(xDiff), abs(yDiff))
        xDiff = xDiff // gcd 
        yDiff = yDiff // gcd 

        if xDiff < 0:
            xDiff *= -1
            yDiff *= -1

        slope = [yDiff, xDiff]

    return slope


def getGreatestCommonDivisor(num1, num2):
    a = num1
    b = num2 
    while True:
        if a == 0:
            return b 
        if b == 0:
            return a 

        a, b = b, a %b


def createHashableKeyForRational(numerator, denominator):
    return str(numerator) + ":" + str(denominator)


if __name__ == '__main__':
    points = [
        [1, 1],
        [2, 2],
        [3, 3],
        [0, 4],
        [-2, 6],
        [4, 0],
        [2, 1],
    ]
    print(aeSolution(points)) # 4