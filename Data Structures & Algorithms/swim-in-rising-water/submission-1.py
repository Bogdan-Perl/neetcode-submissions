class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid) * len(grid[0])
        start = grid[0][0]
        end = grid[-1][-1]
        adjList = self.createAdjList(grid)

        elev = [float('inf')] * n
        elev[start] = start

        minHeap = [(elev[start], start)]
        parent = [-1] * n

        while minHeap:
            curr_elev, u = heapq.heappop(minHeap)
            if u == end:
                break
            if curr_elev < elev[u]:
                continue
            
            for v in adjList[u]:
                new_elev = max(curr_elev, v)
                if new_elev < elev[v]:
                    elev[v] = new_elev
                    heapq.heappush(minHeap, (new_elev, v))
        
        return  elev[end]

        





    def createAdjList(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        adjList = defaultdict(list)
        for r in range(ROWS):
            for c in range(COLS):
                u = grid[r][c]
                #top
                if r >= 1:          adjList[u].append(grid[r-1][c])
                #bottom
                if r < ROWS - 1:    adjList[u].append(grid[r+1][c])
                #left
                if c >= 1:          adjList[u].append(grid[r][c-1])
                #right
                if c < COLS - 1:    adjList[u].append(grid[r][c+1])
        return adjList
