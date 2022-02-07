def specialStrings(strings):
    trie = Trie()
    for string in strings:
        trie.insert(string)
    return findSpecialStrings(strings, trie.root)


def findSpecialStrings(strings, trieNode):
    pass



class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def __repr__(self) -> str:
        return repr(self.root)

    def insert(self, string):
        currentTrieNode = self.root 
        for i in range(len(string)):
            if string[i] not in currentTrieNode:
                currentTrieNode[string[i]] = {}
            currentTrieNode = currentTrieNode[string[i]]
        currentTrieNode[self.endSymbol] = string


if __name__ == '__main__':
    strings = [
        "foobarbaz",
        "foo",
        "bar",
        "foobarfoo",
        "baz",
        "foobaz",
        "foofoofoo",
        "foobazar",
    ]
    print(specialStrings(strings)) # ["foobarbaz", "foobarfoo", "foobaz", "foofoofoo"]