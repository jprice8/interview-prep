from typing import List


class Solution:
    def sumOfSub(self, arr: List[int]) -> int:
        totalSum = 0

        stack = []
        for num in arr:
            while stack and stack[-1] > num:
                stack.pop()
            stack.append(num)

        return totalSum

if __name__ == '__main__':
    s = Solution()
    print(s.sumOfSub([1, 3, 2]))