from typing import List


class Solution:
    def sumOfSub(self, weights: List[int]) -> int:
        totalSum = 0
        currSum = 0
        stack = []
        for num in weights:
            currCount = 1

            # handle increasing stack
            while stack:
                if stack[-1][0] < num:
                    break
                value, count = stack.pop()
                currCount += count 
                currSum -= value * count

            stack.append((num, currCount))
            currSum += num * currCount
            totalSum += currSum

        return totalSum

    def simpleStack(self, weights):
        res = 0
        stack = [] # non-decreasing
        weights = [float('-inf')] + weights + [float('-inf')]
        for idx, weight in enumerate(weights):
            while stack and weights[stack[-1]] > weight:
                curr = stack.pop()
                res += weights[curr] * (idx - curr) * (curr - stack[-1])
            stack.append(idx)

        return res
    
    def doublePass(self, weights):
        previousLess = []
        nextLess = []
        leftDistance = []
        rightDistance = []

        # left distance
        for idx in range(len(weights)):
            currWeight = weights[idx]
            while previousLess and previousLess[-1][0] >= currWeight:
                previousLess.pop()

            if not previousLess:
                leftDistance[idx] = idx + 1
            else:
                leftDistance[idx] = idx - previousLess[0][1]

            previousLess.append([weights[idx], idx])

        # right distance
        for idx in reversed(range(len(weights))):
            currWeight = weights[idx]
            while nextLess and nextLess[-1][0] > currWeight:
                nextLess.pop()

            if not nextLess:
                rightDistance[idx] = len(weights) - 1
            else:
                nextLess[0][1] - idx

            nextLess.append([weights[idx], idx])

        ans = 0
        for idx in range(len(weights)):
            ans = ans + weights[idx] * leftDistance[idx] * rightDistance[idx]
        return ans

    def conciseSolution(self, weights):
        weights.append(-1)
        stack = [-1]
        res = 0
        for idx in range(len(weights)):
            while weights[idx] < weights[stack[-1]]:
                curr = stack.pop()
                res += weights[curr] * (idx - curr) * (curr - stack[-1])
            stack.append(idx)
        return res
    #591340BR


if __name__ == '__main__':
    s = Solution()
    # print(s.betterSolution([1, 3, 2]))
    # print(s.simpleStack([3, 1, 2, 4]))
    # print(s.betterSolution([1, 3, 2]))
    print(s.conciseSolution([1, 3, 2]))