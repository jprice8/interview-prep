import collections
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowLen, colLen = len(board), len(board[0])
        visited = set() # (row, col)
        
        def bfs(coord):
            row, col = coord # (0, 0)
            q = collections.deque() # (row, col, idx)
            q.append((row, col, 0))
            
            while q:
                r, c, wordIdx = q.popleft()
                # check for a match
                if wordIdx + 1 == len(word):
                    return True
                # mark as visited
                visited.add((r, c))
                
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                
                for dr, dc in directions:
                    newRow, newCol = dr + r, dc + c
                    if (0 <= newRow < rowLen and
                        0 <= newCol < colLen and
                        (newRow, newCol) not in visited and
                        board[newRow][newCol] == word[wordIdx + 1]):
                        
                        q.append((newRow, newCol, wordIdx + 1))
        
        for row in range(rowLen):
            for col in range(colLen):
                coord = (row, col)
                # don't BFS if already visited or it's not a potential match of word
                if coord in visited or board[row][col] != word[0]:
                    continue
                
                if bfs(coord):
                    return True
                
        return False

    def existDfs(self, board, word):
        rowLen, colLen = len(board), len(board[0])
        visited, path = set(), set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if ((r, c) in path or
                word[i] != board[r][c] or
                r < 0 or c < 0 or
                r >= rowLen or c >= colLen):
                return False

            # backtrack
            path.add((r, c))
            # neighbors
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in directions:
                newRow, newCol = dr + r, dc + c
                if dfs(newRow, newCol, i + 1):
                    return True
            path.remove((row, col))

            return False

        for row in range(rowLen):
            for col in range(colLen):
                if (row, col) in visited or board[row][col] != word[0]:
                    continue
                # backtrack
                if dfs(row, col, 0):
                    return True

                visited.add((row, col))

        return False

if __name__ == '__main__':
    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    # word = "ABCB"

    board = [['C', 'A', 'A'], ['A', 'A', 'A'], ['B', 'C', 'D']] # true
    word = 'AAB'
    s = Solution()
    print(s.existDfs(board, word))