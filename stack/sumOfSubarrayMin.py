from typing import List


class Solution:
    def sumOfSubarrayMin(self, arr: List[int]) -> int:
        ans = 0
        stack = [] # non-decreasing
        arr = [float('-inf')] + arr + [float("-inf")]
        for idx, val in enumerate(arr):
            while stack and arr[stack[-1]] > val: # Execute if array is decreasing
                stackTop = stack.pop()
                ans += arr[stackTop] * (idx - stackTop) * (stackTop - stack[-1])
            stack.append(idx)
        return ans % (10 ** 9 + 7)

    def sumOfSubarrayMin2(self, arr):
        ans = 0
        stack = []
        arr = [0] + arr + [0]
        for idx, val in enumerate(arr):
            while stack and arr[stack[-1]] > val:
                stackTop = stack.pop()
                peek = stack[-1]
                ans += arr[stackTop] * (idx - stackTop) * (stackTop - peek)
            stack.append(idx)
        return ans % (10 ** 9 + 7)

    def sumOfSubarrayClear(self, arr):
        arr = [0] + arr 
        result = [0] * len(arr)
        stack = [0]
        for i in range(len(arr)):
            while arr[stack[-1]] > arr[i]:
                stack.pop()
            j = stack[-1]
            result[i] = result[j] + (i - j) * arr[i]
            stack.append(i)
        return sum(result) % (10 ** 9 + 7)


if __name__ == '__main__':
    arr = [3, 1, 2, 5, 4]
    s = Solution()
    print(s.sumOfSubarrayClear(arr))