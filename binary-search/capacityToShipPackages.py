import re
from typing import List


class Solution:
    def feasible(self, weights: List[int], max_weight: int, d: int):
        req_days = 1
        capacity = max_weight
        i = 0
        n = len(weights)
        while i < n:
            if weights[i] <= capacity:
                capacity -= weights[i]
                i += 1
            else:
                req_days += 1
                capacity = max_weight
        return req_days <= d

    def feasible1(self, weights, max_weight, d):
        req_days = 1
        capacity = max_weight
        for weight in weights:
            if weight <= capacity:
                capacity -= weight 
            else:
                req_days += 1
                capacity = max_weight
        return req_days <= d

    def min_max_weight(self, weights: List[int], d: int) -> bool:
        left = max(weights)
        right = sum(weights)
        boundary_idx = right
        while left <= right:
            mid = (left + right) // 2
            if self.feasible(weights, mid, d):
                boundary_idx = mid 
                right = mid - 1
            else:
                left = mid + 1
        return boundary_idx

if __name__ == '__main__':
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    d = 5
    s = Solution()
    print(s.min_max_weight(weights, d))