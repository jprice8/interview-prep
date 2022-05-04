from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = pos = neg = 0
        for x in nums: 
            if x > 0: pos, neg = 1 + pos, 1 + neg if neg else 0
            elif x < 0: pos, neg = 1 + neg if neg else 0, 1 + pos
            else: pos = neg = 0 # reset 
            ans = max(ans, pos)
        return ans 

    def maxLength1(self, nums):
        res = pos = neg = 0
        for num in nums:
            if num > 0:
                pos, neg = 1 + pos, 1 + neg if neg else 0 
            elif num < 0:
                pos, neg = 1 + neg if neg else 0, 1 + pos
            else:
                pos = neg = 0
            res = max(res, pos)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.maxLength1([1, -2, -3, 0, 1]))