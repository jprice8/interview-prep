def maxSumIncreasing(array):
    result = []
    finalArray = []
    final = 0

    for i in range(len(array) - 2):
        current = array[i]
        potentialSum = 0

        for j in range(i + 1, len(array) - 1):
            runner = array[j]
            last = array[j - 1]

            if runner < current and runner > last:
                potentialSum += runner

        # Check whether potential > current
        if current > potentialSum:
            final += current
            finalArray.append(current)

    result.append(final)
    result.append(finalArray)


def maxSumIncreasingSolution(array):
    sequences = [None for x in array]
    sums = array[:]
    maxSumIdx = 0

    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
                sums[i] = sums[j] + currentNum
                sequences[i] = j

        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i

    return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]

def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]

    return list(reversed(sequence))



array = [10, 70, 20, 30, 50, 11, 30]
print(maxSumIncreasingSolution(array))