from typing import List


class Solution:
    def subarraySumDivK(self, arr: List[int], k: int) -> int:
        numsSeen = { 0: 1 }
        sumModK = 0
        ans = 0

        for num in arr:
            sumModK = (sumModK + num) % k
            # check if its in there
            if sumModK in numsSeen:
                ans += numsSeen[sumModK]
            # insert into map
            numsSeen[sumModK] = numsSeen.setdefault(sumModK, 0) + 1

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.subarraySumDivK([1, 2, -1, 4, 5], 3))