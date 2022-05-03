import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.suggestions = []

    def add_suggestion(self, product):
        if len(self.suggestions) < 3:
            self.suggestions.append(product)


class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        trie = TrieNode()
        self.addProducts(trie, products)
        
        res, node = [], trie 
        self.collectProducts(res, node, searchWord)
        return res

    def addProducts(self, trie, products):
        for product in products:
            node = trie
            for char in product:
                node = node.children[char]
                node.add_suggestion(product)

    def collectProducts(self, res, node, searchWord):
        for char in searchWord:
            node = node.children[char]
            res.append(node.suggestions)

if __name__ == '__main__':
    s = Solution()
    print(s.suggestedProducts(['mouse', 'mobile', 'moneypot', 'mousepad', 'monitor'], 'mouse'))