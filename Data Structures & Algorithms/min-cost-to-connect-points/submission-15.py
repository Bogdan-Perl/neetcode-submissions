class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        dsu = UnionFind(n)
        minHeap = []
        total = 0

        for i in range(n):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i + 1, n):
                x2, y2 = points[j][0], points[j][1]
                dist = abs(x2 - x1) + abs(y2 - y1)
                edges.append((dist, i, j))

        for d, u, v in edges:
            heapq.heappush(minHeap, (d, u, v))

        while minHeap:
            d, u, v = heapq.heappop(minHeap)
            if dsu.union(u, v):
                total += d
            
        return total



class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * (n+1)

    def find(self, v):
        if v != self.par[v]:
            self.par[v] = self.find(self.par[v])
        return self.par[v]
    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)

        if p1 == p2:
            return False
        if self.rank[p1] >= self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.par[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.par[p1] = p2
        return True
