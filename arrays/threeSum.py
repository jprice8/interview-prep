# n^2 time | O(n) where n is the number of elements in array
def threeSum(array, target):
    result = []
    array.sort()

    for c in range(len(array) - 2):
        l = c + 1
        r = len(array) - 1

        while l < r:
            cs = array[c] + array[l] + array[r]
            if cs == target:
                result.append([array[c], array[l], array[r]])
                l += 1
                r -= 1
            elif cs < target:
                l += 1
            elif cs > target:
                r -= 1

    return result



array = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0
print(threeSum(array, target))