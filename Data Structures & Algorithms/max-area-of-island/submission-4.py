class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxCount = 0
        def dfs(grid, r, c):
            counter = 0
            if (min(r, c) < 0 or r == ROWS or c == COLS or not grid[r][c]):
                return 0
            elif grid[r][c]:
                counter = 1
            
            grid[r][c] = 0

            counter += dfs(grid, r, c+1)
            counter += dfs(grid, r-1, c)
            counter += dfs(grid, r, c-1)
            counter += dfs(grid, r+1, c)

            return counter
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    maxCount = max(maxCount, dfs(grid, r, c))
        return maxCount