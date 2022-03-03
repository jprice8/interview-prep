import collections


class Solution:
    def solutionDFS(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or (r, c) in visited or grid[r][c] == "0":
                return 

            visited.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        return islands

    def solutionBFS(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                visited.add((row, col))
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and 
                        grid[r][c] == '1' and
                        (r, c) not in visited):
                        q.append((row + dr, col + dc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)
        return islands


if __name__ == '__main__':
    grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    s = Solution()
    # print(s.solutionDFS(grid)) # 3
    print(s.solutionBFS(grid)) # 3