from collections import Counter


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


if __name__ == '__main__':
    nums = [3, 1, 2, 5, 1]
    k = 3
    print(subarraySumDivisibleByK(nums, k))


