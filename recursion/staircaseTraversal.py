# O(s^h) time | O(h) space - where h is height and s is the number of steps (maxSteps).
def staircaseTraversal1(height, maxSteps):
    return numberOfWaysToTop(height, maxSteps)


def numberOfWaysToTop(height, maxSteps):
    if height <= 1:
        return 1

    numberOfWays = 0
    for step in range(1, min(maxSteps, height) + 1):
        numberOfWays += numberOfWaysToTop(height - step, maxSteps)

    return numberOfWays


# O(s*h) time | O(h) space 
def staircaseTraversal2(height, maxSteps):
    return numberOfWaysToTop2(height, maxSteps, {0: 1, 1: 1})


def numberOfWaysToTop2(height, maxStep, memo):
    if height in memo: return memo[height]
    if height <= 1:
        return 1

    numberOfWays = 0
    for step in range(1, min(height, maxStep) + 1):
        numberOfWays += numberOfWaysToTop2(height - step, maxStep, memo)

    memo[height] = numberOfWays
    return numberOfWays


# O(s*h) time | O(h) space
def staircaseTraversal3(height, maxSteps):
    waysToTop = [0 for _ in range(height + 1)]
    waysToTop[0] = 1
    waysToTop[1] = 1

    for currentHeight in range(2, height + 1):
        step = 1
        while step <= maxSteps and step <= currentHeight:
            waysToTop[currentHeight] = waysToTop[currentHeight] + waysToTop[currentHeight - step]
            step += 1

    return waysToTop[height]

#O(n) time | O(n) space - where n is height
def staircaseTraversal4(height, maxSteps):
    currentNumberOfWays = 0
    waysToTop = [1]

    for currentHeight in range(1, height + 1):
        startOfWindow = currentHeight - maxSteps - 1
        endOfWindow = currentHeight - 1
        if startOfWindow >= 0:
            currentNumberOfWays -= waysToTop[startOfWindow]

        currentNumberOfWays += waysToTop[endOfWindow]
        waysToTop.append(currentNumberOfWays)

    return waysToTop[height]


if __name__ == '__main__':
    # print(staircaseTraversal1(4, 2))
    # print(staircaseTraversal1(200, 2))

    # print(staircaseTraversal2(4, 2)) # 5
    # print(staircaseTraversal2(200, 2))

    # print(staircaseTraversal3(4, 2)) # 5

    print(staircaseTraversal4(4, 2)) # 5