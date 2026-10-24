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

        mst = 0
        minHeap = []
        visted = set([0])
        total = 0
        for d, v in adjList[0]:
            heapq.heappush(minHeap, (d, 0, v))

        while  mst < len(points) - 1:
            d, u, v = heapq.heappop(minHeap)
            if v in visted: 
                continue
            visted.add(v)
            total += d
            mst += 1

            for d2, nxt in adjList[v]:
                if nxt not in visted:
                    heapq.heappush(minHeap, (d2, v, nxt))

        return total


        
