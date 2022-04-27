from collections import Counter


class Solution:
    def findLeast(self, arr, k):
        c = Counter(arr)
        cnt, remaining = Counter(c.values()), len(c)
        for key in range(1, len(arr) + 1):
            if k >= key * cnt[key]:
                k -= key * cnt[key]
                remaining -= cnt[key]
            else:
                return remaining - k // key 
        return remaining

if __name__ == '__main__':
    s = Solution()
    print(s.findLeast([5, 5, 4], 1))