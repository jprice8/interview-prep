def howSum(targetSum, numbers):
    if targetSum == 0: return []
    if targetSum < 0: return None 

    for num in numbers:
        remainder = targetSum - num 
        remainderResult = howSum(remainder, numbers)
        if remainderResult is not None:
            remainderResult.append(num)
            return remainderResult

    return None


def howSumMemo(targetSum, numbers, memo=None):
    # We do the following because Python evaluates defualt argument in def line, not on function call.
    if memo is None:
        memo = {}
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None 

    for num in numbers:
        remainder = targetSum - num 
        memo[targetSum] = howSumMemo(remainder, numbers, memo)
        if memo[targetSum] is not None:
            memo[targetSum].append(num)
            return memo[targetSum]

    return None


if __name__ == '__main__':
    # print(howSum(7, [2, 3])) # [3, 2, 2]
    # print(howSum(7, [5, 3, 4, 7])) # [4, 3]
    # print(howSum(7, [2, 4])) # None
    # print(howSum(8, [2, 3, 5])) # [2, 2, 2, 2]
    # print(howSum(300, [7, 14])) # None

    print(howSumMemo(7, [2, 3])) # [3, 2, 2]
    print(howSumMemo(7, [5, 3, 4, 7])) # [4, 3]
    print(howSumMemo(7, [2, 4])) # None
    print(howSumMemo(8, [2, 3, 5])) # [2, 2, 2, 2]
    print(howSumMemo(300, [7, 14])) # None

    # Brute Force
    # time: O(n^m) where n is the length of the array and m is the targetSum / height of the recursion tree
    # space: O(m) where m is the targetSum / height of the recursion tree

    # Memoized
    # time: O(m*n)