from typing import List


class Trie:
    def __init__(self):
        self.root = {}
        self.end = '*'
        
    def insert(self, s: str):
        node = self.root 
        for char in s:
            node = node.setdefault(char, {})
        node[self.end] = self.end
        
    def words_with_matches(self, s: str) -> List[str]:
        # s = 'be'
        res = []
        node = self.root 
        for char in s:
            if not char in node:
                return []
            node = node.get(char)
            
        self.collect_words(node, s, res)
        return res
            
    def collect_words(self, node, s, res):
        for key in node:
            if key == self.end:
                res.append(s)
                continue
            self.collect_words(node[key], s + key, res)
                

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        
        # 1) build the prefix tree
        trie = Trie()
        for product in products:
            trie.insert(product)
        
        # 2) Loop through the search word and collect hits for each substring
        for i in range(len(searchWord)):
            substring = searchWord[:i + 1] # 'm', 'mo', 'mou'...
            matching_products = trie.words_with_matches(substring) # ['mobile', 'moneypot', 'monitor'...]
            # sort lexi #O(nlog(n))
            matching_products.sort()
            # return up to top three
            res.append(matching_products[:3])
            
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.suggestedProducts(['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad'], 'mouse'))