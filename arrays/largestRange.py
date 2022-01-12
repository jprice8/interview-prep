def largestRange(array):
    # Sort array
    array.sort()

    minRange = float('inf')
    maxRange = float('-inf')

    for i in range(1, len(array)):
        num = array[i]
        # Is current the next number in range?
        if num == array[i - 1] + 1:
            maxRange = num 
        else:
            minRange = num 
            maxRange = num

    return [minRange, maxRange]


def largestRangeHash(array):
    bestRange = []
    longestLength = 0
    nums = {}
    for num in array:
        nums[num] = True
    for num in array:
        if not nums[num]:
            continue
        nums[num] = False
        currentLength = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            currentLength += 1
            left -= 1

        while right in nums:
            nums[right] = False 
            currentLength += 1
            right += 1

        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left + 1, right - 1]
    return bestRange


if __name__ == '__main__':
    print(largestRangeHash([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6])) # [0, 7]