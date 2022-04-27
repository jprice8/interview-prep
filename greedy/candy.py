from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        cache = [1] * len(ratings)

        # left to right pass
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                cache[i] = cache[i - 1] + 1

        # right to left pass
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                cache[i] = max(cache[i + 1] + 1, cache[i])

        # sum cached candies
        return sum(cache)


if __name__ == '__main__':
    s = Solution()
    print(s.candy([1, 3, 4, 5, 2])) # 11
