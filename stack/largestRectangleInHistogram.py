from typing import List


class Solution:
    def largestRect(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > h:
                # pop
                index, height = stack.pop()
                # calculate height
                max_area = max(max_area, height * (i - index))
                # extend current heigh backwards
                start = index 
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area

if __name__ == '__main__':
    s = Solution()
    print(s.largestRect([2, 1, 5, 6, 2, 3])) # 10