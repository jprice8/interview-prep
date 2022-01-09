def bestSum(targetSum, numbers):
    if targetSum == 0: return [] 
    if targetSum < 0: return None

    minResult = None

    for num in numbers:
        remainder = targetSum - num 
        remainderResult = bestSum(remainder, numbers)
        if remainderResult is not None:
            remainderResult.append(num)
            if minResult is None or len(minResult) > len(remainderResult):
                minResult = remainderResult

    return minResult


if __name__ == '__main__':
    print(bestSum(7, [5, 3, 4, 7]))
    # print(bestSum(8, [2, 3, 8]))
    # print(bestSum(8, [1, 4, 5]))
    # print(bestSum(100, [1, 2, 5, 25]))