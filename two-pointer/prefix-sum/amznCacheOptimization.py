from typing import List


class Solution:
    def cacheOptiBrute(self, power: List[int]) -> int:
        totalPower = 0
        for i in range(len(power)):
            for j in range(i, len(power)):
                subArray = power[i:j + 1]
                subSum = sum(subArray)
                subMin = min(subArray)
                totalPower += subMin * subSum

        return totalPower % 10 ** 7 


if __name__ == '__main__':
    power = [2, 3, 2, 1]
    s = Solution()
    print(s.cacheOptiBrute(power))