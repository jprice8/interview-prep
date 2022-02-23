# O(n * m * 4^w) time | 
class Solution:
    def wordSearch(board, word):
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True 
            if (r < 0 or c < 0 
                or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False 

            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or 
                   dfs(r - 1, c, i + 1) or 
                   dfs(r, c + 1, i + 1) or 
                   dfs(r, c - 1, i + 1))

            path.remove((r, c))
            return res

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0): return True 

        return False


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E'],
    ]
    word = 'SEE'
    s = Solution()
    print(s.wordSearch(board, word))