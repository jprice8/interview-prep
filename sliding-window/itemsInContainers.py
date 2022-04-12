from typing import List


class Solution:
    def itemsInContainers(self, s: str, startIndices: List[int], endIndices: List[int]) -> List[int]:
        # handle edge case
        if len(s) < 2:
            return [0]

        # instantiate variables
        result = []

        # find idx of first pipe
        leftMostPipeIdx = -1
        for idx, char in enumerate(s):
            if char == '|':
                leftMostPipeIdx = idx
                break

        # find idx of last pipe
        rightMostPipeIdx = -1
        for idx in reversed(range(len(s))):
            char = s[idx]
            if char == '|':
                rightMostPipeIdx = idx
                break

        # handle no pipe pairs in string
        if leftMostPipeIdx == -1 or rightMostPipeIdx == -1:
            return [0]

        # loop through index pairs
        for i in range(len(startIndices)):
            # convert to zero indexed
            startIdx = startIndices[i] - 1
            endIdx = endIndices[i] - 1

            # find max of startIdx or left most pipe
            trueStartIdx = max(startIdx, leftMostPipeIdx)
            trueEndIdx = min(endIdx, rightMostPipeIdx)
            # loop through true range and count stars
            starCount = 0
            for charIdx in range(trueStartIdx, trueEndIdx + 1):
                char = s[charIdx]
                if char == '*':
                    starCount += 1

            if starCount > 0:
                result.append(starCount)

        return result

if __name__ == '__main__':
    s = "*|*|*|*"
    startIndices = [1, 1]
    endIndices = [1, 6]
    solution = Solution()
    print(solution.itemsInContainers(s, startIndices, endIndices))