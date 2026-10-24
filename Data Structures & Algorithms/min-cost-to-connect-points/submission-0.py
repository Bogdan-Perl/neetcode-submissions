class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u in range(len(points)):
            for v in range(len(points)):
                w = abs(points[v][0] - points[u][0]) + abs(points[v][1] - points[u][1])
                graph[u].append((w, v))
        
        visted = set()
        heap = []
        total_weight = 0
        visted.add(0)
        for w, v in graph[0]:
            heapq.heappush(heap, (w, 0, v))
        while heap:
            w, u, v = heapq.heappop(heap)
            if v in visted:
                continue
            visted.add(v)
            total_weight += w
            for w2, nxt in graph[v]:
                if nxt not in visted:
                    heapq.heappush(heap, (w2, v, nxt))
        return total_weight

