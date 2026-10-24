class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        
        queue = deque([(0, 0, 1)])
        vist = set((0, 0))

        while queue:
            r, c, length = queue.popleft()
            
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c]:
                continue
            if r == ROWS - 1 and c == COLS - 1:
                return length

            for dr, dc in directions:
                if (r+dr, c+dc) not in vist:
                    queue.append((r + dr, c + dc, length + 1))
                    vist.add((r + dr, c + dc))
        return -1
        









'''
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque([(0, 0, 1)])
        vist = set((0, 0))
        neighbors = [[0,-1], [0, 1], [-1, 0], [1, 0], [1,1], [-1, -1], [1, -1], [-1, 1]]

        while q:
            r, c, length = q.popleft()

            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 1:
                continue
            if r == ROWS - 1 and c == COLS - 1:
                return length
            
            for dr, dc in neighbors:
                if (r+dr, c+dc) not in vist:
                    q.append((r+dr, c+dc, length + 1))
                    vist.add((r+dr, c+dc))
                
        return -1
            
'''