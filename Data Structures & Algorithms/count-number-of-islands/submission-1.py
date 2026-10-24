class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visted = [[False for _ in range(COLS)]for _ in range(ROWS)]
        islands = 0
        def dfs(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS
                or visted[r][c] or grid[r][c] == "0"):
                return 
            
            visted[r][c] = True
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and not visted[r][c]:
                    dfs(r, c)
                    islands += 1
        return islands