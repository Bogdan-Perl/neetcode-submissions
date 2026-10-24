class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = []
        graph = defaultdict(list)

        for idx1, p1 in enumerate(points):
            for idx2, p2 in enumerate(points):
                if p1 is p2:
                    continue
                graph[idx1].append(((abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])), idx2))

        heap = []
        total = 0
        visted = set()
        start = 0
        visted.add(start)

        for w, v in graph[start]:
            heapq.heappush(heap, (w, start, v))
        
        while heap:
            w, u, v = heapq.heappop(heap)
            if v in visted:
                continue
            visted.add(v)
            total += w

            for w2, nxt in graph[v]:
                if nxt not in visted:
                    heapq.heappush(heap, (w2, v, nxt))

        return total


