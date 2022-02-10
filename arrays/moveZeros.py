def moveZeros(nums):
    fastPtr = 0
    slowPtr = 0
    while fastPtr < len(nums):
        if nums[fastPtr] != 0:
            nums[slowPtr], nums[fastPtr] = nums[fastPtr], nums[slowPtr]
            slowPtr += 1

        fastPtr += 1

    return nums


if __name__ == '__main__':
    # nums = [3, 1, 0, 1, 3, 8, 9]
    nums = [1, 0, 2, 0, 0, 7]
    print(moveZeros(nums))