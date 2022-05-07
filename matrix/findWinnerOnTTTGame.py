from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        rows, cols = [0] * n, [0] * n
        diag = anti_diag = 0
        
        # player1 goes first
        player = 1
        
        for row, col in moves:
            
            # update the values for move
            rows[row] += player
            cols[col] += player
            
            # Update diagonal if required
            if row == col:
                diag += player
            if row + col == n - 1:
                anti_diag += player
                
            # validate for winner
            if any(abs(line) == n for line in (rows[row], cols[col], diag, anti_diag)):
                return 'A' if player == 1 else 'B'
            
            # change player if noone has won
            player *= -1
            
        # If all moves done and still no winner, return draw
        return 'Draw' if len(moves) == n * n else 'Pending'

if __name__ == '__main__':
    s = Solution()
    print(s.tictactoe())