from typing import List


class Solution:
    def wordLadder(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        


if __name__ == '__main__':
    wordList = ['hot', 'lot', 'log', 'dot', 'dog', 'cog']
    s = Solution()
    print(s.wordLadder('hit', 'cog', wordList))