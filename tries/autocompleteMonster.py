
# Not counting building Trie, my best guess
# O(c^2 + mlog(m))
def autocomplete(repository, customerQuery):
    trie = buildTrie(repository) 

    results = []
    # For every char in query after idx 1
    for charIdx in range(2, len(customerQuery) + 1):
        queryToMatch = customerQuery[:charIdx]

        prefixMatches = trie.findPrefixMatch(queryToMatch)
        prefixMatches.sort()
        prefixMatches = prefixMatches[:3]
        results.append(prefixMatches)

    return results

class Trie:
    def __init__(self):
        self.root = {}
        self.end = "#"

    def insert(self, word):
        node = self.root 
        for char in word:
            node = node.setdefault(char, {})
        node[self.end] = self.end

    def findPrefixMatch(self, queryToMatch):
        node = self.root 
        for char in queryToMatch:
            if char not in node:
                return []
            node = node[char]
        ans = []
        self._findPrefixMatchHelper(node, queryToMatch, ans)
        return ans

    def _findPrefixMatchHelper(self, node, queryToMatch, ans):
        for key in node:
            if key == self.end:
                ans.append(queryToMatch)
                continue 
            self._findPrefixMatchHelper(node[key], queryToMatch + key, ans)



def buildTrie(repository):
    trie = Trie()
    for word in repository:
        trie.insert(word)

    return trie


if __name__ == '__main__':
    repository = [
        'mobile',
        'mouse',
        'moneypot',
        'monitor',
        'mousepad'
    ]
    customerQuery = "mouse"
    print(autocomplete(repository, customerQuery))
