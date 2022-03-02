from typing import List


# O(n) time | O(1) space - where n is the length of height.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        
        while l < r:
            distance = r - l
            current_area = min(height[l], height[r]) * distance
            max_area = max(max_area, current_area)
            
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
                
        return max_area