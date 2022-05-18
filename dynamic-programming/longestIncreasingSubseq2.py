class Solution:
    def longestSub(self, arr):
        def dfs(startIdx, path):
            nonlocal longestSub
            if startIdx == len(arr):
                return

            for i in range(startIdx, len(arr)):
                path.append(arr[i])
                dfs(i + 1, path)

        longestSub = 0
        dfs(0)
        return longestSub

if __name__ == '__main__':
    s = Solution()
    print(s.longestSub([1, 2, 4, 3]))