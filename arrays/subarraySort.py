def subarraySort(array):
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")

    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i, num, array):
            minOutOfOrder = min(num, minOutOfOrder)
            maxOutOfOrder = max(num, maxOutOfOrder)

    if minOutOfOrder == float("inf"):
        return [-1, -1]

    # Find sorted index of minOutOfOrder
    left = 0
    while array[left] < minOutOfOrder:
        left += 1

    # Find sorted index of minOutOfOrder
    right = len(array) - 1
    while array[right] > maxOutOfOrder:
        right -= 1

    return [left, right]


def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num > array[i + 1] or num < array[i - 1]



if __name__ == '__main__':
    print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])) # [3, 9]