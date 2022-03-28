from typing import List


class Solution:
    def planPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        points = 0
        windowSum = 0
        left = 0
        for right in range(len(calories)):
            windowSum += calories[right]
            # Start left window when "k" width is reached
            windowLength = right - left + 1
            if windowLength > k:
                windowSum -= calories[left]
                left += 1
                
            if windowLength >= k:
                # calculate points
                if windowSum < lower:
                    points -= 1
                elif windowSum > upper:
                    points += 1
            
        return points

    def planPerformance1(self, calories, k, lower, upper):
        point, win = 0, sum(calories[:k - 1])
        for i, calorie in enumerate(calories[k - 1:], k - 1):
            win += calorie - (i >= k) * calories[i - k]
            point += (win > upper) - (win < lower)
        return point

if __name__ == '__main__':
    # calories = [3, 2]
    # k = 2
    # lower = 0
    # upper = 1

    calories = [6, 5, 0, 0]
    k = 2
    lower = 1
    upper = 5
    s = Solution()
    print(s.planPerformance1(calories, k, lower, upper))