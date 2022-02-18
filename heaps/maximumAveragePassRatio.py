import heapq


def maxAvgPassRatio(classes, extraStudents):
    maxHeap = []

    for passing, total in classes:
        maxHeap.append((-calculateGain(passing, total), passing, total))
    heapq.heapify(maxHeap)

    for _ in range(extraStudents):
        maxGain, passing, total = heapq.heappop(maxHeap)
        maxGain *= -1
        newGain = calculateGain(passing + 1, total + 1)
        heapq.heappush(maxHeap, (-newGain, passing + 1, total + 1))

    return sum(a / b for g, a, b in maxHeap) / len(classes)


def calculateGain(a, b):
    currentPR = a / b
    potentialPR = (a + 1) / (b + 1)
    return potentialPR - currentPR


if __name__ == '__main__':
    classes = [
        [1, 2],
        [3, 5],
        [2, 2]
    ]
    extraStudents = 2 
    print(maxAvgPassRatio(classes, extraStudents)) # 0.78333

    # classes2 = [
    #     [2, 4],
    #     [3, 9],
    #     [4, 5],
    #     [2, 10]
    # ]
    # extraStudents2 = 4
    # print(maxAvgPassRatio(classes2, extraStudents2))