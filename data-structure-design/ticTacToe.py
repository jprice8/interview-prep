class TicTacToe:
    def __init__(self, n: int):
        self.board = self.buildBoard(n)
        self.playerMap = {
            1: 'X',
            2: 'O'
        }
        
    def buildBoard(self, n):
        board = []
        for row in range(n):
            tmpBoard = []
            for col in range(n):
                tmpBoard.append('#')
            board.append(tmpBoard)
            
        return board
        
    def move(self, row: int, col: int, player: int) -> int:
        # 1) Place piece
        self.board[row][col] = self.playerMap[player]
        
        # 2) Check for winner
        return self.checkForWinner(row, col, player)
        
    def checkForWinner(self, row, col, player) -> int:
        # Horizontal
        for row in self.board:
            rowSet = set(row)
            if len(rowSet) == 1 and '#' not in rowSet:
                return player
            
        # Vertical
        verticalSet = set([])
        for row in self.board:
            verticalSet.add(row[col])
        if len(verticalSet) == 1 and '#' not in verticalSet:
            return player
        
        # Diagonal
        diagonalSet1 = set([])
        col = 0
        for row in self.board:
            diagonalSet1.add(row[col])
            col += 1
        if len(diagonalSet1) == 1 and '#' not in diagonalSet1:
            return player

        diagonalSet2 = set([])
        col = 0
        for rowIdx in reversed(range(len(self.board))):
            diagonalSet2.add(self.board[rowIdx][col])
            col += 1
        if len(diagonalSet2) == 1 and '#' not in diagonalSet2:
            return player
        
        # If no winners, return loser
        return 0

if __name__ == '__main__':
    ttt = TicTacToe(2)
    print(ttt.move(0, 1, 1))
    print(ttt.move(1, 1, 2))
    print(ttt.move(1, 0, 1))