from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False
        
        # determine which rows/cols need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
                        
        # zero out needed r/c
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
                    
        
        # edge case 1
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
                
        # edge case 2
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0


if __name__ == '__main__':
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    s = Solution()
    print(s.setZeroes(matrix))