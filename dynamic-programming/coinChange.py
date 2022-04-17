from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(coins, remain, memo):
            if remain in memo:
                return memo[remain]
            if remain == 0:
                # handle base save state
                return 0
            if remain < 0:
                # handle base discard
                return -1

            minCount = float('inf')
            for coin in coins:
                count = dfs(coins, remain - coin, memo)
                if count == -1: continue
                minCount = min(minCount, count + 1)

            memo[remain] = minCount
            return minCount if minCount != float('inf') else -1

        return dfs(coins, amount, {})

if __name__ == '__main__':
    coins = [2, 3, 5]
    s = Solution()
    print(s.coinChange(coins, 8))