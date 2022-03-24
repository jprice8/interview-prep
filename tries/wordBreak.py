from typing import List


class PrefixTree:
    def __init__(self):
        self.root = {}
        self.end = "*"

    def insert(self, word):
        node = self.root 
        for c in word:
            node = node.setdefault(c, {})
        node[self.end] = self.end


class Solution:
    def wordBreakTrie(self, s: str, wordDict: List[str]) -> bool:
        prefixTree = PrefixTree()
        for w in wordDict:
            prefixTree.insert(w)

        found = 0
        for left in range(len(s)):
            right = left 
            node = prefixTree.root
            while right < len(s) and s[right] in node:
                node = node[s[right]]
                if prefixTree.end in node:
                    found += (right - left) + 1
                right += 1

        return found == len(s)

    def wordBreakRecursive(self, s: str, wordDict: List[str], memo=None) -> bool:
        if memo is None:
            memo = {}
        if s in memo: return memo[s]
        if s == '': return True

        for word in wordDict:
            if s.find(word) == 0:
                substring = s[len(word):]
                memo[s] = self.wordBreakRecursive(substring, wordDict, memo)
                if memo[s]: return True

        return False


if __name__ == '__main__':
    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]
    solution = Solution()
    # print(solution.wordBreakTrie(s, wordDict)) # False
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(solution.wordBreakRecursive(s, wordDict))