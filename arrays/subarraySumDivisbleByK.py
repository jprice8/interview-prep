from collections import Counter
import collections


def subarraySumDivisibleByK(nums, k):
    remainders = Counter({0: 1})
    current_sum = 0
    count = 0
    for i in range(len(nums)):
        num = nums[i]
        current_sum += num 
        remainder = current_sum % k 
        complement = (k - remainder) % k
        if complement in remainders:
            count += remainders[complement]
        remainders[complement] += 1

    return count 

from collections import defaultdict


def solution2(nums, k):
    hashMap = defaultdict(int)
    hashMap[0] = 1
    prefix = 0
    result = 0

    for num in nums:
        prefix = (prefix + num) % k

        if prefix in hashMap:
            result += hashMap[prefix]

        hashMap[prefix] += 1

    return result

def solution3(nums, k):
    result = 0
    prefixSumCount = collections.defaultdict(int)
    prefixSumCount[0] += 1
    runningCalc = 0

    for num in nums:
        runningCalc = (runningCalc + num) % k

        if runningCalc in prefixSumCount:
            result += prefixSumCount[runningCalc]

        prefixSumCount[runningCalc] += 1

    return result


if __name__ == '__main__':
    # nums = [3, 1, 2, 5, 1]
    # k = 3

    nums = [4, 5, 0, -2, -3, 1]
    k = 5
    print(solution3(nums, k)) # 7


