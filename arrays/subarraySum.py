from collections import defaultdict
import collections


def subarraySum(array, target):
    prefix_sums = {0: 0}
    cur_sum = 0
    for i in range(len(array)):
        cur_sum += array[i]
        complement = cur_sum - target 
        if complement in prefix_sums:
            return [prefix_sums[complement], i + 1]
        prefix_sums[cur_sum] = i + 1


def subarraySum2(nums, k):
    result = 0
    prefixSum = 0
    hashMap = defaultdict(int)
    hashMap[0] = 1

    for num in nums:
        prefixSum += num

        if prefixSum - k in hashMap:
            result += hashMap[prefixSum - k]

        hashMap[prefixSum ] += 1

    return result


def bruteForce(nums, k):
    result = 0
    for i in range(len(nums)):
        tmpResult = 0
        for j in range(i, len(nums)):
            tmpResult += nums[j]
            if tmpResult == k:
                result += 1

    return result


# O(n) time | O(n) space - where n is the length of nums
def optimalSolution(nums, k):
    result = 0
    prefixSumCount = collections.defaultdict(int)
    prefixSumCount[0] += 1
    runningSum = 0

    for num in nums:
        runningSum += num 
        delta = runningSum - k
        if delta in prefixSumCount:
            result += prefixSumCount[delta]

        prefixSumCount[runningSum] += 1

    return result


if __name__ == '__main__':
    # array = [1, 3, -3, 8, 5, 7]
    # target = 5
    nums = [1, 1, 1]
    k = 2
    # print(subarraySum2(nums, k)) # 2

    nums2 = [1, 6, 3]
    k2 = 3
    # print(subarraySum2(nums2, k2)) # 2

    # num3 = [3, 4, 7, 2, -3, 1, 4, 2]
    # k3 = 7 
    print(optimalSolution(nums2, k2))