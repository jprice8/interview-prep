import collections


class Solution:
    def uniqueLetterStrings(self, s: str) -> int:
        """
        1) The maximum possible substrings that can end at an index are i + 1.
        2) The contribution of a character to this substring is (i + 1) - it's last seen position.
        3) At each point, sum of all contributions gives the number of total substrings found so far.
        4) The last seen position of char is actually i + 1.
        """
        last_position = collections.defaultdict(int) # Used for storing the last position of each character.
        contribution = collections.defaultdict(int) # Used for storing the contribution of each char so far.
        res = 0

        for i, char in enumerate(s):
            max_possible_substrs_at_idx = i + 1
            contribution[char] = max_possible_substrs_at_idx - last_position[char]

            res += sum(contribution.values())
            last_position[char] = i + 1

        return res

    # def layedOutSolution(self, s: str) -> int:
    #     d = collections.defaultdict(lambda: (0, 0))
    #     dp = [0] * (len(s) + 1)
    #     for i, c in enumerate(s, 1):
    #         dp[i] = dp[i - 1] + i - 2 * (d[c][1] - d[c][0]) - d[c][0]
    #         d[c] = (d[c][1], 1)
    #     return sum(dp)


if __name__ == '__main__':
    s = "ABA"
    solution = Solution()
    print(solution.uniqueLetterStrings(s))
    # print(solution.layedOutSolution(s))