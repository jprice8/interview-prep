class TicTacToe:
    def __init__(self, n):
        self.n = n
        self.horiz = [0] * n 
        self.vert = [0] * n 
        self.diag1 = 0
        self.diag2 = 0

    def move(self, row, col, player):
        n = self.n 
        move = 1 if player == 1 else -1

        self.horiz[col] += move 
        self.vert[row] += move 

        if row == col:
            self.diag1 += move 
        if row + col == (n - 1):
            self.diag2 += move 

        if abs(self.horiz[col])==n or abs(self.vert[row])==n or abs(self.diag1)==n or abs(self.diag2)==n:
            return player
        return 0


if __name__ == '__main__':
    ttt = TicTacToe(3)
    print(ttt.move(0, 0, 1))
    print(ttt.move(0, 2, 2))
    print(ttt.move(2, 2, 1))
    print(ttt.move(1, 1, 2))
    print(ttt.move(2, 0, 1))
    print(ttt.move(1, 0, 2))
    print(ttt.move(2, 1, 1))