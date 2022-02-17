# O(n) time | O(n) space - where n is the length of nums.
def productExceptSelf(nums):
    length = len(nums)

    leftProducts, rightProducts, result = [0] * length, [0] * length, [0] * length

    leftProducts[0] = 1
    for i in range(1, length):
        leftProducts[i] = nums[i - 1] * leftProducts[i - 1]

    rightProducts[length - 1] = 1
    for i in reversed(range(length - 1)):
        rightProducts[i] = nums[i + 1] * rightProducts[i + 1]

    for i in range(length):
        result[i] = leftProducts[i] * rightProducts[i]

    return result


# O(n) time | O(1) space
def optimalProductExceptSelf(nums):
    length = len(nums)
    result = [0] * length

    result[0] = 1
    for i in range(1, length):
        result[i] = nums[i - 1] * result[i - 1]


    right = 1
    for i in reversed(range(length)):
        result[i] = result[i] * right 
        right *= nums[i]

    return result


def aeSolution(array):
    products = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    for i in range(len(array)):
        products[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in reversed(len(array)):
        products[i] *= rightRunningProduct
        rightRunningProduct *= array[i]

    return products


if __name__ == '__main__':
    nums = [4, 5, 1, 8, 2]
    # nums = [1, 2, 3, 4]
    print(aeSolution(nums))