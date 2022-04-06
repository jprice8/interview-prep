from typing import List


class Solution:
    def wordbreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(i):
            if len(i) == len(s):
                return True 

            for word in wordDict:
                if s[i:].startswith(word):
                    if dfs(i + len(word)):
                        return True

            return False

        return dfs(0)

if __name__ == '__main__':
    s = Solution()
    print(s.wordbreak("applepenapple", ["apple", "pen"]))