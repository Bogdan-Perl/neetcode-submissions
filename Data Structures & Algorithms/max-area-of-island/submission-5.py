class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        visted = set()
        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or (r,c) in visted or not grid[r][c]:
                return 0
            
            res = 1
            visted.add((r, c))
            res += dfs(r + 1, c)
            res += dfs(r - 1, c)
            res += dfs(r, c + 1)
            res += dfs(r, c -1)
            
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and (r, c) not in visted:
                    maxArea = max(maxArea, dfs(r, c))
        return maxArea

        