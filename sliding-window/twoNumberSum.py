
def twoNumberSum(array, targetSum):
    hashtable = {}

    for idx, val in enumerate(array):
        hashtable[val] = idx 

    for idx, val in enumerate(array):
    
        delta = targetSum - val

        if delta in hashtable:
            # Find idx of delta in hashtable, if any
            deltaIdx = hashtable[delta]
            # If the found delta is not the current idexed number, return
            if deltaIdx != idx:
                return [delta, val]

    return []
    

# print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))

def aeSolutionHashtable(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num 
        if potentialMatch in nums:
            return [potentialMatch, num]

        else:
            nums[num] = True 

    return []

print(aeSolutionHashtable([3, 5, -4, 8, 11, 1, -1, 6], 10))