

def sortedSquareArray(array):
    newArray = []

    start = 0
    end = len(array) - 1

    while start <= end:
        startValue = array[start]
        endValue = array[end]
        if abs(startValue) > abs(endValue):
            newArray.insert(0, startValue * startValue)
            start += 1
        else:
            newArray.insert(0, endValue * endValue)
            end -= 1

    return newArray


print(sortedSquareArray([-4, 1, 2, 3, 5, 6, 7]))