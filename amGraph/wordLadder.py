import collections
from typing import List


# hot -> *ot, h*t, ho*
# lot -> *ot, l*t, lo*

class Solution:
    def wordLadder(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # build adj list
        adjList = collections.defaultdict(list)
        for i in range(len(wordList)):
            word = wordList[i]
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:]
                adjList[pattern].append(word)

        visited = set()
        res = 1
        q = collections.deque([beginWord])
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1:]
                    for neighbor in adjList[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)

            res += 1
        return 0


if __name__ == '__main__':
    wordList = ['hot', 'lot', 'log', 'dot', 'dog', 'cog']
    s = Solution()
    print(s.wordLadder('hit', 'cog', wordList))
