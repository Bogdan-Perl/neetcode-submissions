class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        total = 0
        rotten  = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    total += 1
                if grid[r][c] == 2:
                    rotten += 1
                    q.append((r, c, 0))

        if total == rotten:
            return 0

        while q:
            r, c, t = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    rotten += 1
                    if total == rotten:
                        return t + 1

                    q.append((nr, nc, t + 1))

        return -1

        
        
