def longestIncreasingSubsequence(array):
    result = []
    longestSub = recursiveHelper(array, result)
    return longestSub


def recursiveHelper(array, result):
    if len(array) == 0:
        return


if __name__ == '__main__':
    array = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35] # [-24, 2, 3, 5, 6, 35]
    print(longestIncreasingSubsequence(array))