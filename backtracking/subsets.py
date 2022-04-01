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


if __name__ == '__main__':
    popularity = [3, 5, -2]
    s = Solution()
    print(s.subsets(popularity))