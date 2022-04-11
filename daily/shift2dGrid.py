from typing import List
import copy


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        num_rows, num_cols = len(grid), len(grid[0])
        copyGrid = copy.deepcopy(grid)
        
        for row in range(num_rows):
            for col in range(num_cols):
                new_col = (col + k) % num_cols
                wrap_around_count = (col + k) // num_cols
                new_row = (row + wrap_around_count) % num_rows
                grid[new_row][new_col] = copyGrid[row][col]
            
        return grid


if __name__ == '__main__':
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s = Solution()
    print(s.shiftGrid(grid, 4))