import heapq


class Solution:
    def uglyNumber1(self, n: int) -> bool:
        if n == 0: return False 
        while n % 5 == 0: n /= 5
        while n % 3 == 0: n /= 3 
        while n % 2 == 0: n /= 2
        return n == 1

    def uglyNumber2(self, n: int) -> int:
        allowed_prime = (2, 3, 5)
        ans_heap = [1]
        used_nums = {1}
        for _ in range(n - 1):
            val = heapq.heappop(ans_heap)
            for multiplier in allowed_prime:
                if val * multiplier not in used_nums:
                    heapq.heappush(ans_heap, val * multiplier)
                    used_nums.add(val * multiplier)
        return ans_heap[0]

    def uglyNumber2merge(self, n):
        q2, q3, q5 = [2], [3], [5]
        ugly = 1
        for u in heapq.merge(q2, q3, q5):
            if n == 1:
                return ugly 
            if u > ugly:
                ugly = u 
                n -= 1
                q2 += 2 * u,
                q3 += 3 * u,
                q5 += 5 * u,


if __name__ == '__main__':
    s = Solution()
    print(s.uglyNumber2(10))