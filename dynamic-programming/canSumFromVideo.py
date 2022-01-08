def canSum(targetSum, numbers, memo = {}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return True 
    if targetSum < 0: return False 

    for num in numbers:
        remainder = targetSum - num 
        memo[targetSum] = canSum(remainder, numbers, memo)
        if memo[targetSum]: return True

    return False

    # for num in numbers:
    #     remainder = targetSum - num 
    #     if canSum(remainder, numbers, memo) == True:
    #         memo[targetSum] = True 
    #         return True 

    # memo[targetSum] = False 
    # return False


if __name__ == '__main__':
    print(canSum(7, [2, 3], {})) # True
    print(canSum(7, [5, 3, 4, 7], {})) # True
    print(canSum(7, [2, 4], {})) # False
    print(canSum(8, [2, 3, 5], {})) # True
    print(canSum(300, [7, 14], {})) # False