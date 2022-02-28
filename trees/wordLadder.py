import collections
import string
from typing import List


def wordLadder(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0

    neighbors = collections.defaultdict(list)
    wordList.append(beginWord)
    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j + 1]
            neighbors[pattern].append(word)

    visit = set([beginWord])
    q = collections.deque([beginWord])
    res = 1
    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return res 

            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                for neighborWord in neighbors[pattern]:
                    if neighborWord not in visit:
                        visit.add(neighborWord)
                        q.append(neighborWord)
        result += 1

    return 0


class Leetcode:
    def laddLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        wordLength = len(beginWord)

        all_combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(wordLength):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i]  + "*" + word[i+1:]].append(word)

        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing the same word
        visited = {beginWord: True}

        while queue:
            current_word, level = queue.popleft()
            for i in range(wordLength):
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]

                # All the words which share the same intermediate state
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True 
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []

        return 0


def epiSolution(beginWord, endWord, wordList):
    StringWithDistance = collections.namedtuple(
        'StringWithDistance', ('candidate_string', 'distance')
    )
    q = collections.deque([StringWithDistance(beginWord, 0)])
    visited = {beginWord: True}

    while q:
        currentTuple = q.popleft()
        if currentTuple.candidate_string == endWord:
            return currentTuple.distance

        # Tries all possible transformations of candidate string
        for i in range(len(currentTuple.candidate_string)):
            for j in string.ascii_lowercase:
                candidate = currentTuple.candidate_string[:i] + j + currentTuple.candidate_string[i + 1:]
                if candidate not in visited and candidate in wordList:
                    visited[candidate] = True 
                    q.append(StringWithDistance(candidate, currentTuple.distance + 1))
    return 0


class Solution:
    def wordLadder(self, beginWord, endWord, wordList):
        q = collections.deque()
        


if __name__ == '__main__':
    # beginWord = 'hit'
    # endWord = 'cog'
    # wordList = ['hot', 'dot', 'dog', 'lot', 'log']

    beginWord = 'a'
    endWord = 'c'
    wordList = [
        'a',
        'b',
        'c'
    ]
    # print(wordLadder(beginWord, endWord, wordList))
    # leetcode = Leetcode()
    # print(leetcode.laddLength(beginWord, endWord, wordList))
    # print(epiSolution(beginWord, endWord, wordList))

    s = Solution()
    print(s.wordLadder(beginWord, endWord))