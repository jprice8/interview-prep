from typing import List


class Solution:
    def subsets(self, popularity: List[int]):
        n = len(popularity)
        output = [[]]

        for num in popularity:
            output += [curr + [num] for curr in output]

        sum_list = []
        for subset in output:
            sum_list.append(sum(subset))

        sum_list.sort(reverse=True)

        return sum_list[:3]

    def subsetsRecursion(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, used, res):
            # base
            if len(path) == len(nums):
                res.append(path[:])
                return 

            # children
            for idx, num in enumerate(nums):
                # have we seen num before?
                if used[idx]:
                    continue 

                # recursion
                path.append(num)
                used[idx] = True
                dfs(path, used, res)
                path.pop()
                used[idx] = False

        res = []
        dfs([], [False] * len(nums), res)
        return res


if __name__ == '__main__':
    popularity = [3, 5, -2]
    s = Solution()
    print(s.subsetsRecursion(popularity))