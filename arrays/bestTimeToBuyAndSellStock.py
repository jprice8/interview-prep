class Solution:
    def buyAndSell(self, prices):
        left = 0
        right = 0
        maxProfit = 0

        while right <  len(prices):
            leftPrice = prices[left]
            rightPrice = prices[right]
            # if right < left
            if leftPrice > rightPrice:
                left = right 
            elif leftPrice < rightPrice:
                currentProfit = rightPrice - leftPrice
                maxProfit = max(maxProfit, currentProfit)
                right += 1
            else:
                right += 1

        return maxProfit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    s = Solution()
    print(s.buyAndSell(prices))