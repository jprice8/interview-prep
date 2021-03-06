from typing import List


class Node:
    def __init__(self):
        self.root = {}
        self.end = "#"

    def insert(self, word: str) -> None:
        node = self.root 
        for c in word:
            node = node.setdefault(c, {})
        node[self.end] = self.end


class Solution:
    def horizontalScan(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        for idx, val in enumerate(shortest):
            for word in strs:
                if word[idx] != val:
                    return shortest[:idx]

        return shortest

    def verticalScan(self, strs: List[str]) -> str:
        pass 

    def divideAndConquer(self, strs):
        pass 

    def binarySearch(self, strs):
        pass 

    def trieSolution(self, strs):
        pass 


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    s = Solution()
    print(s.horizontalScan(strs))
    # print(s.verticalScan(strs))
    # print(s.divideAndConquer(strs))
    # print(s.binarySearch(strs))