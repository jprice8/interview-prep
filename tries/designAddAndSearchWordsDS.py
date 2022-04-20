class WordDictionary:
    def __init__(self):
        self.root = {}
        self.end = '*'

    def addWord(self, word: str) -> None:
        node = self.root 
        for char in word:
            node = node.setdefault(char, {})
        node[self.end] = True

    def searchLc2(self, word: str) -> bool:
        def dfs(j, node):
            for i in range(j, len(word)):
                char = word[i]
                # is char not in word?
                if not char in node:
                    # recursive call or return false
                    if char == '.':
                        for key in node.keys():
                            if key != '*' and dfs(i + 1, node[key]):
                                return True
                    return False
                else:
                    node = node[char]
            return self.end in node
        return dfs(0, self.root)


if __name__ == '__main__':
    wd = WordDictionary()
    # print(wd.addWord('bad'))
    # print(wd.addWord('dad'))
    # print(wd.addWord('mad'))
    # print(wd.search('pad')) 
    # print(wd.search('bad')) 
    # print(wd.search('.ad')) # true
    # print(wd.search('b..')) # true
    print(wd.addWord('a'))
    print(wd.addWord('a'))
    print(wd.searchLc2('.a')) # false
    print(wd.searchLc2('a.')) # false