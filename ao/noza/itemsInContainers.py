from typing import List
from collections import Counter
import bisect


class Solution:
    # def itemsInContainers(self, s: str, startIndices: List[int], endIndices: List[int]) -> List[int]:
    def numberOfItems(self, s, startIndices, endIndices):
        result = []
        n = len(startIndices)
        for i in range(n):
            # establish current range (zero indexed)
            currStartIdx = startIndices[i] - 1
            currEndIdx = endIndices[i] - 1
            
            # find first pipe for right and left boundary
            left, right = currStartIdx, currEndIdx
            # find first left pipe
            while s[left] != '|' and left < right:
                left += 1
                
            while s[right] != '|' and left < right:
                right -= 1
            
            starCount = 0
            # loop through new piped range to collect stars
            for charIdx in range(left, right):
                if s[charIdx] == '*':
                    starCount += 1
                    
            if starCount > 0:
                result.append(starCount)
                
        return result if result else [0]




def numberOfItems(s, startIndices, endIndices):
    n = len(s)
    # left most pipe
    stars = [0] * (n + 1)
    leftPipeIdx = [-1] * (n + 1)
    for i, char in enumerate(s, 1):
        if char == "|":
            stars[i] = stars[i - 1]
            leftPipeIdx[i] = leftPipeIdx[i - 1]
    if leftPipeIdx[-1] == -1:
        return [0] * len(startIndices)
    
    # right most pipe
    rightPipeIdx = [n + 1] * (n + 1)
    for i in range(n - 1, -1, -1):
        if s[i] == '|':
            rightPipeIdx[i + 1] = i + 1
        else:
            rightPipeIdx[i + 1] = rightPipeIdx[i + 2] if i < n - 1 else n + 1
            
    # calc anser
    ans = []
    for i in range(len(startIndices)):
        si, ei = startIndices[i], endIndices[i]
        leftPipe = rightPipeIdx[si]
        rightPipe = leftPipeIdx[ei]
        ans.append(stars[rightPipe] - stars[leftPipe] if leftPipe < rightPipe else 0)
    return ans

def numberOfItems(s, startIndices, endIndices):
    pipes, stars = [], 0
    pdic = Counter()
    for i, ch in enumerate(s):
        if ch == "|":
            pdic[i] = stars
            pipes.append(i)
        elif pipes:
            stars += 1
    if not pipes:
        return [0] * len(startIndices)
    
    ans = []
    for idx in range(len(startIndices)):
        si, ei = startIndices[idx], endIndices[idx]
        spi = bisect.bisect_left(pipes, si)
        epi = bisect.bisect_right(pipes, ei) - 1
        ans.append(pdic[pipes[epi]] - pdic[pipes[spi]])
    return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfItems('|**|*|*', [1, 1], [5, 6]))