# O(n^4) time | O(1) space
# def maximizeExpression(array):
#     if len(array) < 4:
#         return 0

#     maximumValueFound = float("-inf")

#     for a in range(len(array)):
#         aValue = array[a]
#         for b in range(a + 1, len(array)):
#             bValue = array[b]
#             for c in range(b + 1, len(array)):
#                 cValue = array[c]
#                 for d in range(c + 1, len(array)):
#                     dValue = array[d]
#                     expressionValue = evaluateExpression(aValue, bValue, cValue, dValue)
#                     maximumValueFound = max(maximumValueFound, expressionValue)

#     return maximumValueFound


# def evaluateExpression(a, b, c, d):
#     return a - b + c - d


def maximizeExpression(array):
    if len(array) < 4:
        return 0

    maxOfA = [array[0]]
    maxOfAMinusB = [float("-inf")]
    maxOfAMinusBPlusC = [float("-inf")] * 3
    maxOfAMinusBPlusCMinusD = [float("-inf")] * 3

    for idx in range(1, len(array)):
        currentMax = max(maxOfA[idx - 1], array[idx])
        maxOfA.append(currentMax)

    #### TBContinued ####


if __name__ == '__main__':
    array = []
    print(maximizeExpression(array))