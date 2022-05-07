import collections
import heapq
from typing import List


class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.words = []  # [(count, sentence), (count, sentence)]

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = Trie()
        self.countCache = {}
        self.keyword = ''

        for idx, sen in enumerate(sentences):
            self._insert(sen, self.root)
            self.countCache[sen] = times[idx]

    def _insert(self, word, node):
        for char in word:
            node = node.children[char]
            node.words.append(word)

    def _find(self, word):
        node = self.root 
        for char in word:
            node = node.children[char]
        return node.words

    def input(self, c: str) -> List[str]:
        if c != '#':
            self.keyword = self.keyword + c 
            words = self._find(self.keyword)
            res = []
            for word in words:
                res.append((self.countCache[word], word))
            res = list(set(res))
            res.sort(key=lambda x: (-x[0], x[1]))
            return [i[1] for i in res[:3]]
        else:
            self.countCache[self.keyword] = self.countCache.get(self.keyword, 0) + 1
            self._insert(self.keyword, self.root)
            self.keyword = ''
            return []


if __name__ == '__main__':
    sentences = ['i love you', 'ironman', 'i love lucy', 'island']
    times = [5, 3, 2, 2]
    obj = AutocompleteSystem(sentences, times)
    print(obj.input('i'))
    print(obj.input(' '))
    print(obj.input('a'))
    print(obj.input('#'))
