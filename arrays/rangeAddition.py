from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0] * length
        
        for start, end, value in updates:
            ans[start] += value
            end += 1
            if end < len(ans):
                ans[end] -= value
                
        for i in range(1, len(ans)):
            ans[i] += ans[i - 1]
            
        return ans


if __name__ == '__main__':
    length = 5
    updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
    s = Solution()
    print(s.rangeAddition(length, updates))