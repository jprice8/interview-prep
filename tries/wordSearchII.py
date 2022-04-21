import collections
from typing import List


class Trie:
    def __init__(self):
        self.root = {}
        self.end = '*'

    def insert(self, word):
        node = self.root 
        for char in word:
            node = node.setdefault(char, {})
        node[self.end] = self.end


class Solution:
    def buildTree(self, words: List[str]) -> Trie:
        prefixTree = Trie()
        for word in words:
            prefixTree.insert(word)
        return prefixTree

    def bfs(self, coord, visited, pTree, res, numRows, numCols, board, currWord):
        q = collections.deque([])
        q.append(coord)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc 
                if (0 <= newRow < numRows and
                    0 <= newCol < numCols and
                    not (newRow, newCol) in visited and 
                    board[newRow][newCol] in pTree):
                    # add to curr word
                    q.append((newRow, newCol))
                    visited.add((newRow, newCol))
                    pTree = pTree[board[newRow][newCol]]
                    currWord.append(board[newRow][newCol])

        # check if pTree is at star,
        if '*' in pTree:
            newWord = ''.join(currWord)
            res.append(newWord)

    def wordSearch(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        # set board constraints
        numRows, numCols = len(board), len(board[0])
        # build the prefix tree
        pTree = self.buildTree(words)
        visited = set([])
        # Loop through the board cells and perform BFS
        for row in range(numRows):
            for col in range(numCols):
                cellChar = board[row][col] # "o"
                cellCoord = (row, col)
                # check if char is in pTree, not in visited
                if not cellChar in pTree.root or cellCoord in visited:
                    continue 

                # move root up level
                root = pTree.root
                root = root[cellChar]
                visited.add(cellCoord)
                currWord = [cellChar]
                # perform BFS
                self.bfs(cellCoord, visited, root, res, numRows, numCols, board, currWord)

        return res




if __name__ == '__main__':
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v'],
    ]
    words = ['oath', 'pea', 'eat', 'rain']
    s = Solution()
    print(s.wordSearch(board, words))