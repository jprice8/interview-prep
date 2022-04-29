from math import gcd


class Solution:
    def nthMagicalNumberMath(self, n: int, a: int, b: int):
        MOD = 10 ** 9 + 7

        l = a / gcd(a, b) * b 
        m = l / a + l / b - 1
        q, r = divmod(n, m)

        if r == 0:
            return q * l % MOD

        heads = [a, b]
        for _ in range(r):
            if heads[0] <= heads[1]:
                heads[0] += a 
            else:
                heads[1] += b 
        
        return (q * l + min(heads)) % MOD

    # O(n*a*b) time | O(n*a*b)
    def nthMagicalNumberBinarySearch(self, N: int, A: int, B: int):
        a, b = A, B
        while b: a, b = b, a % b
        l, r, lcm = 2, 10 ** 14, A * B / a 
        while l < r:
            m = (l + r) / 2
            if m / A + m / B - m / lcm < N:
                l = m + 1 
            else: 
                r = m 
        return l % (10 ** 9 + 7)

if __name__ == '__main__':
    s = Solution()
    # print(s.nthMagicalNumberMath(4, 2, 3)) # 6
    print(s.nthMagicalNumberBinarySearch(4, 2, 3)) # 6