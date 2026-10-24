class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c, vist):
            if (min(r, c) < 0 or r == ROWS or c == COLS
                or (r, c) in vist or grid[r][c]):
                return 0
            if r == ROWS -1 and c == COLS -1:
                return 1
            res = 0
            vist.add((r,c))
            res += dfs(r-1, c, vist)
            res += dfs(r+1, c, vist)
            res += dfs(r, c-1, vist)
            res += dfs(r, c+1, vist)
            vist.remove((r,c))
            return res
        return dfs(0, 0, set())