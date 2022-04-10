from typing import List


class Solution:
    def countNiceSubs(self, nums: List[int], k: int) -> int:
        res = 0
        # loop through nums
        for i in range(len(nums)):
            odds = 0
            for j in range(i, len(nums)):
                # check num is odd
                if nums[j] % 2 != 0:
                    odds += 1
                # check if subarray has at least k odds
                if odds == k:
                    res += 1

        return res

    def countNiceSubsAM(self, nums, k):
        # sake of easier calcs
        odd_indices = [-1]
        for idx, val in enumerate(nums):
            if val % 2 != 0:
                odd_indices.append(idx)
        if len(odd_indices) <= k:
            return 0

        res = 0
        # sake of easier calcs
        odd_indices.append(len(nums))
        for idx in range(len(odd_indices) - k - 1):
            start_diff = odd_indices[idx + 1] - odd_indices[idx]
            end_diff = odd_indices[idx + k + 1] - odd_indices[idx + k]
            res += start_diff * end_diff
        return res

    def prefixSum(self, nums, k):
        numMap = { 0: 1 }
        count, res = 0, 0
        for idx, num in enumerate(nums):
            if num % 2 == 1:
                count += 1
            
            if count - k in numMap:
                res += numMap[count - k]

            numMap[count] = numMap.get(count, 0) + 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.prefixSum([1, 1, 2, 1, 1], 3)) # 2