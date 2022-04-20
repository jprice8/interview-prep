class Trie:

    def __init__(self):
        self.root = {}
        self.end = '*'

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end] = self.end

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root 
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

if __name__ == '__main__':
    trie = Trie()
    print(trie.insert('app'))
    print(trie.insert('apple'))
    print(trie.insert('beer'))
    print(trie.insert('add'))
    print(trie.insert('jam'))
    print(trie.insert('rental'))
    print(trie.search('apps')) # false
    print(trie.search('app')) # true