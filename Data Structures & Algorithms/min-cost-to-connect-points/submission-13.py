class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))

        
        mst = []
        minHeap = []
        total = 0
        start = 0
        visted = set([start])
        for dist, v in adjList[start]:
            heapq.heappush(minHeap, (dist, start, v))

        while len(mst) < len(points) - 1:
            w, u, v = heapq.heappop(minHeap)
            if v in visted:
                continue
            total += w
            mst.append((w, u, v))
            visted.add(v)
            for w2, nxt in adjList[v]:
                if nxt not in visted:
                    heapq.heappush(minHeap, (w2, v, nxt))
        
        return total


        