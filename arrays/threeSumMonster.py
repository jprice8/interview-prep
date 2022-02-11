# def triplets_with_sum_0(nums):
#     resultDict = {}
#     nums.sort()

#     for idx in range(len(nums) - 2):
#         left = idx + 1
#         right = len(nums) - 1

#         while left < right:
#             threeSum = nums[left] + nums[right] + nums[idx]
#             if threeSum < 0:
#                 left += 1
#             elif threeSum > 0:
#                 right -= 1
#             else:
#                 tmpArray = [nums[idx], nums[left], nums[right]]
#                 resultDict[idx] = True
#                 left += 1
#                 right -= 1


#     resultArray = []
#     for key in resultDict.keys():
#         resultArray.append(key)

#     resultArray.sort()
#     return resultArray
        

from collections import Counter


def triplets_with_sum_0(nums):
    num_count = Counter(nums)
    unique_nums = sorted(num_count.keys())
    results = []

    for i, first_num in enumerate(nums):
        num_count[first_num] -= 1
        for j in range(i, len(unique_nums)):
            second_num = unique_nums[j]
            third_num = -first_num - second_num
            if third_num < second_num:
                break 
            if num_count[second_num] <= 0:
                continue
            num_count[second_num] -= 1
            if num_count.get(third_num, 0) <= 0:
                num_count[second_num] += 1
                continue
            results.append([first_num, second_num, third_num])
            num_count[second_num] += 1
        num_count[first_num] += 1
    return results



if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(triplets_with_sum_0(nums)) # [[-1, -1, 2], [-1, 0, 1]]