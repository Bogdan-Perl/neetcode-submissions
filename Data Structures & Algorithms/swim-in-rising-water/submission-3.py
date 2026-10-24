class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def gridToAdjList(grid):
            graph = defaultdict(list)

            nei = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            for r in range(ROWS):
                for c in range(COLS):
                    node = (r, c)

                    for dr, dc in nei:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS:
                            graph[node].append(((nr, nc), grid[nr][nc]))

            return graph


        graph = gridToAdjList(grid)
        visted = set()

        heap = [(grid[0][0], (0, 0))]
        times = [[float('inf') for _ in range(COLS)] for _ in range(ROWS)]
        times[0][0] = grid[0][0]


        while heap:
            curr_time, node = heapq.heappop(heap)
            r, c = node
            

            if r == ROWS-1 and c == COLS-1:
                break
            if node in visted:
                continue
            visted.add(node)

            for nnode, t in graph[node]:
                nr, nc = nnode
                new_time = max(curr_time, t)
                if new_time <= times[nr][nc]:
                    times[nr][nc] = new_time
                    heapq.heappush(heap, (new_time, (nr, nc)))


        return times[ROWS - 1][COLS - 1] if times[ROWS - 1][COLS - 1] != float('inf') else -1





