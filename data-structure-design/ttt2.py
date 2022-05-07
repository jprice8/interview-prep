class TicTacToe:

    def __init__(self, n: int):
        self.row, self.col = [0] * n, [0] * n 
        self.diag, self.anti_diag = 0, 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        offset = player * 2 - 3 
        self.row[row] += offset 
        self.col[col] += offset 
        if row == col:
            self.diag += offset 
        if row + col == self.n - 1:
            self.anti_diag += offset 
        if self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 2 
        if -self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 1
        return 0


if __name__ == '__main__':
    ttt = TicTacToe(3)
    print(ttt.move(0,0,1))
    print(ttt.move(1,1,1))
    print(ttt.move(2,2,1))
    # print(ttt.move(1,1,2))
    # print(ttt.move(2,0,1))
    # print(ttt.move(1,0,2))
    # print(ttt.move(2,1,1))