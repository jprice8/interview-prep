from collections import deque
from functools import lru_cache
import math


# def maxScore(nums: List[int]) -> int:
#     highScore = 0

#     for i in range(len(nums) - 1):
#         level = 1

#         for j in range(i + 1, len(nums)):
#             score = level * gcd(nums[i], nums[j])
#             highScore = max(highScore, score)

#         level += 1

#     return highScore


def maxScoreTopDown(nums):
    @lru_cache(None)
    def dfs(i, mask):
        if i > len(nums) // 2:
            return 0
        res = 0
        for j in range(len(nums)):
            for k in range(j + 1, len(nums)):
                new_mask = (1 << j) + (1 << k)
                if not mask & new_mask:
                    res = max(res, i * math.gcd(nums[j], nums[k]) + dfs(i + 1, mask + new_mask))

        return res 
    return dfs(1, 0)


def maxScoreBottomUp(nums):
    scores = [0] * (1 << len(nums))
    full = len(scores) - 1
    queue = deque([0])
    level = 0
    while queue:
        level += 1
        row = len(queue)
        for _ in range(row):
            mask = queue.popleft()
            for i in range(len(nums)):
                if mask & (1 << i):
                    continue
                for j in range(i + 1, len(nums)):
                    if mask & (1 << j):
                        continue 
                    m = mask | (1 << i) | (1 << j)
                    score = scores[mask] + level * math.gcd(nums[i], nums[j])
                    scores[m] = max(scores[m], score)
                    if m != full:
                        queue.append(m)
    return scores[-1]


def cyberGeekSolution(nums):
    def calc_score(nums, scores):
        if not nums:
            return 0
        if tuple(nums) in scores:
            return scores[tuple(nums)]
        n = len(nums) / 2
        maxScore = 0
        for i in range(int(2*n)):
            for j in range(i+1, int(2*n)):
                a = nums[i]
                b = nums[j]
                nums_copy = nums.copy()
                nums_copy.remove(a)
                nums_copy.remove(b)
                score = int(n*math.gcd(a,b) + calc_score(nums_copy, scores))
                if score > maxScore:
                    maxScore = score 
        scores[tuple(nums)] = maxScore
        return maxScore
    return calc_score(nums, {})

if __name__ == '__main__':
    nums = [3, 4, 6, 8]
    # print(cyberGeekSolution(nums))
    # print(maxScoreBottomUp(nums))
    print(maxScoreTopDown(nums))