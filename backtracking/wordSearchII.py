import collections


class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.isWord = False

    def insert(self, word):
        node = self
        for char in word:
            node = node.children[char]
        node.isWord = True

class Solution:
    def findWords(self, board, words):
        rowLen, colLen = len(board), len(board[0])
        res, path = set(), set()
        
        def dfs(r, c, node, word):
            # base case
            if (r < 0 or c < 0 or
                r >= rowLen or c >= colLen or
                (r, c) in path or
                board[r][c] not in node.children):
                return
            
            # recursive call to neighbors
            node = node.children[board[r][c]]
            word += board[r][c]
            path.add((r, c))
            if node.isWord:
                res.add(word)

            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                newRow, newCol = r + dr, c + dc
                dfs(newRow, newCol, node, word)
            path.remove((r, c))

        root = Trie()
        for word in words:
            root.insert(word)
        
        for row in range(rowLen):
            for col in range(colLen):
                dfs(row, col, root, '')

        return list(word)


if __name__ == '__main__':
    board = [
        ["o", "a", "a", "n"], 
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"], 
        ["i", "f", "l", "v"]
    ]
    words = ["oath", "pea", "eat", "rain", "hklf", "hf"]
    s = Solution()
    print(s.findWords(board, words))
