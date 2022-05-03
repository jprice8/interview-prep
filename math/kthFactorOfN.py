class Solution:
    def kthFactor(self, n, k):
        factors = [num for num in range(1, n + 1) if n % num == 0]
        
        i = 0
        while i < len(factors) and i <= k:
            if i == k:
                return factors[i]
            i += 1
            
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.kthFactor(12, 3))