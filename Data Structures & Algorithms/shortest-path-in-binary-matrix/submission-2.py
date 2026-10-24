class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        if grid[0][0]: return -1

        queue.append((0,0))
        vist = set((0,0))
        length = 1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS-1 and c == COLS-1: return length
                neighbors = [[1,0], [-1,0], [0,1], [0,-1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

                for dr, dc in neighbors:
                    if (min(r + dr, c + dc) < 0 or r + dr == ROWS or c + dc==COLS
                        or (r + dr, c + dc) in vist or grid[r + dr][c + dc]):
                        continue
                    queue.append((r + dr, c + dc))
                    vist.add((r + dr, c + dc))
                
            length += 1
        return -1





