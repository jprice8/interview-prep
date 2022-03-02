class Solution:
    def countBits(self, n):
        ans = [0 for _ in range(n + 1)]
        for x in range(1, n + 1):
            ans[x] = ans[x & (x - 1)] + 1
        return ans


if __name__ == '__main__':
    n = 8 
    s = Solution()
    print(s.countBits(n))