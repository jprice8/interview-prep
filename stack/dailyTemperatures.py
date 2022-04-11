from typing import List


class Solution:
    def dailyTemp(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        
        for idx, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                topIdx = stack.pop()
                ans[topIdx] = idx - topIdx
            stack.append(idx)
            
        return ans


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    s = Solution()
    print(s.dailyTemp(temperatures))