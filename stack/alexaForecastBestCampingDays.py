from typing import List


class Solution:
    def idealDays(self, days: List[int], k: int) -> List[int]:
        n = len(days)
        ans = []
        leftIdeal = [0 for _ in range(n)]
        rightIdeal = [0 for _ in range(n)]
        for i in range(1, n):
            if days[i] <= days[i - 1]:
                leftIdeal[i] = leftIdeal[i - 1] + 1

        for i in reversed(range(n - 1)):
            if days[i] <= days[i + 1]:
                rightIdeal[i] = rightIdeal[i + 1] + 1


if __name__ == '__main__':
    days = [3, 2, 2, 2, 3, 4]
    k = 2
    s = Solution()
    print(s.idealDays(days, k))