class Solution:
    def groupByCharacter(self, s: str) -> int:
        groups = [1]
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i - 1], groups[i])
        return ans

    def linearScan(self, s: str) -> int:
        ans, prev, curr = 0, 0, 1
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                ans += min(prev, curr)
                prev, curr = curr, 1
            else:
                curr += 1

        return ans + min(prev, curr)


if __name__ == '__main__':
    string = "111000110010"
    s = Solution()
    print(s.groupByCharacter(string))
    # print(s.linearScan(string))