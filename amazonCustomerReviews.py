

class PrefixTrie:
    def __init__(self):
        self.root = {}
        self.end = "*"

    def __repr__(self) -> str:
        return repr(self.root)

    def insertWord(self, word):
        node = self.root 
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end] = True

    def insertRepo(self, repo):
        for word in repo:
            self.insertWord(word)

    def wordsWithPrefix(self, prefix):
        """
        Given the prefix, return the top results that match
        in the repo. Sort results by alphabetical order.
        """
        node = self.root
        # List of list for results
        ans = []

        # Iterate through characters in the given prefix
        for char in prefix:
            tmp = []
            if char not in node:
                break

            # Call collect words helper
            self.collectWords(node, prefix, tmp)
            node = node[char]
            ans.append(tmp)

        return ans

    def collectWords(self, node, prefix, ans):
        """
        Return a list of all matching words from prefix.
        """
        for key in node:
            if key == self.end:
                ans.append(prefix)
                continue

            self.collectWords(node[key], prefix + key, ans)


def searchSuggestions(repository, customerQuery):
    trie = PrefixTrie() 
    trie.insertRepo(repository)

    results = trie.wordsWithPrefix(customerQuery)
    return results

if __name__ == '__main__':
    repository = ['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad']
    customerQuery = 'mouse'

    print(searchSuggestions(repository, customerQuery))