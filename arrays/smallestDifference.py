def smallestDifference(array1, array2):
    smallest = float('inf')
    smallestNums = []
    array1.sort()
    array2.sort()

    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        num1 = array1[i]
        num2 = array2[j]
        delta = abs(num1 - num2)
        if delta == 0:
            return [num1, num2]
        if delta < smallest:
            smallest = delta
            smallestNums = [num1, num2]
        if num2 > num1:
            i += 1
        else:
            j += 1

    return smallestNums


def smallestDifferenceSolution(array1, array2):
    array1.sort()
    array2.sort()
    idxOne = 0
    idxTwo = 0

    smallest = float('inf')
    current = float('inf')
    smallestPair = []

    while idxOne < len(array1) and idxTwo < len(array2):
        firstNum = array1[idxOne]
        secondNum = array2[idxTwo]

        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        if current < smallest:
            smallest = current 
            smallestPair = [firstNum, secondNum]

    return smallestPair


if __name__ == '__main__':
    array1 = [-1, 5, 10, 20, 28, 3]
    array2 = [26, 134, 135, 15, 17]
    print(smallestDifference(array1, array2))
