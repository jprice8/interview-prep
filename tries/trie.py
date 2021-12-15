#https://leetcode.com/problems/implement-trie-prefix-tree/discuss/412299/Python3-Solution-with-ALL-trie-operations-including-finding-all-words-with-some-prefix

class Trie:
    def __init__(self) -> None:
        """
        Initialize data structure.
        """
        self.root = {}
        self.end = "#"

    def __repr__(self) -> str:
        return repr(self.root)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.end] = self.end

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return self.end in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True

    def allWords(self) -> list:
        """
        Return all words in the trie.
        """
        node = self.root
        ans = []
        self._collect(node, '', ans)
        return ans

    def _collect(self, node, path: str, ans: list) -> None:
        """
        Helper function to collect nodes.
        """
        for k in node:
            if k == self.end:
                ans.append(path)
                continue
            self._collect(node[k], path + k, ans)

    def words_with_prefix(self, prefix: str) -> list:
        """
        Return all possible words with common prefix.
        """
        node = self.root
        for c in prefix:
            if c not in node:
                return []
            node = node[c]
        ans = []
        self._words_with_prefix_helper(node, prefix, ans)
        return ans

    def _words_with_prefix_helper(self, node, prefix: str, ans: list) -> None:
        """
        Helper function to recursively traverse nodes.
        """
        for k in node:
            if k == self.end:
                ans.append(prefix)
                continue 
            self._words_with_prefix_helper(node[k], prefix + k, ans)

if __name__ == '__main__':
    trie = Trie()
    trie.insert('mobile')
    trie.insert('mouse')

    print(trie)

    print(trie.words_with_prefix('mou'))
