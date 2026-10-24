class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u in range(len(points)):
            for v in range(len(points)):
                w = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                graph[u].append((w, v))
                graph[v].append((w, u))
        
        visted = set()
        start = 0
        heap = []
        total_weight = 0

        for w, v in graph[start]:
            heapq.heappush(heap, (w, start, v))
        
        while heap:
            w, u, v = heapq.heappop(heap)
            if v in visted:     continue
            visted.add(v)
            total_weight += w

            for w2, nxt in graph[v]:
                if nxt not in visted:
                    heapq.heappush(heap, (w2, v, nxt))
        return total_weight


