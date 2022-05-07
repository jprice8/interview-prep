import collections
from typing import List


class Solution:
    def twoQueues(self, nums: List[int], limit: int) -> int:
        maxq = collections.deque()
        minq = collections.deque()
        i = 0
        for num in nums:
            while maxq and num > maxq[-1]:
                maxq.pop()
            while minq and num < minq[-1]:
                minq.pop()

            maxq.append(num)
            minq.append(num)

            # if bust
            if maxq[0] - minq[0] > limit:
                if maxq[0] == nums[i]:
                    maxq.popleft()
                if minq[0] == nums[i]:
                    minq.popleft()
                i += 1
        return len(nums) - i


if __name__ == '__main__':
    s = Solution()
    print(s.twoQueues([8,2,4,7], 4))