from typing import List


class PrefixTree:
    def __init__(self):
        self.root = {}
        self.end = '*'

    def __repr__(self) -> str:
        return repr(self.root)

    def insertWord(self, word):
        node = self.root
        for i in range(len(word)):
            currentChar = word[i]
            node = node.setdefault(currentChar, {})
        node[self.end] = self.end

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]

        return self.end in node


class Solution:
    # O(m * n) time -> building trie | O(m * n) space
    def indexPairsOfString(self, text: str, words: List[str]) -> List[List[int]]:
        # Build prefix tree
        prefixTree = PrefixTree()
        for w in words:
            prefixTree.insertWord(w)

        ans = []
        for i in range(len(text)):
            j = i
            node = prefixTree.root 
            while j < len(text) and text[j] in node:
                node = node[text[j]]
                if prefixTree.end in node:
                    ans.append([i, j])
                j += 1
        return ans

    # O((n^2 * m) + (mlog(m)) time | O(m) space where n is the length of text, m is the length of words, 
    def naiveSolution(self, text: str, words: List[str]) -> List[List[int]]:
        ans = []
        for w in words:
            l, r = 0, len(w) - 1
            while r < len(text):
                textSubstring = text[l:r + 1]
                if w == textSubstring:
                    ans.append([l, r])

                l += 1
                r += 1

        ans.sort(key=lambda x: (x[0], x[1]))
        return ans


if __name__ == '__main__':
    # text = "thestoryofleetcodeandme"
    # words = ["story", "fleet", "leetcode"]
    s = Solution()
    # print(s.indexPairsOfString(text, words)) # [[3, 7], [9, 13], [10, 17]]
    text = "ababa"
    words = ["aba", "ab"]
    # print(s.naiveSolution(text, words)) # [[0, 1], [0, 2], [2, 3], [2, 4]]
    print(s.indexPairsOfString(text, words)) # [[0, 1], [0, 2], [2, 3], [2, 4]]