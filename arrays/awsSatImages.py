import collections


class Solution:
    def findMaximumGraynes(self, arr):
        rows = collections.defaultdict(int)
        cols = collections.defaultdict(int)

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        
        maxG = float('-inf')
        rowLength = len(arr)
        colLength = len(arr[0])
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                continue

        return maxG


if __name__ == '__main__':
    arr = [[1, 0, 1], [0, 0, 1], [1, 1, 0]]
    s = Solution()
    print(s.findMaximumGraynes(arr))