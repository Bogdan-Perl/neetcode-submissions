class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        dsu = UnionFind(n)

        for i in range(n):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i + 1, n):
                x2, y2 = points[j][0], points[j][1]
                dist = abs(x2 - x1) + abs(y2 - y1)
                edges.append((dist, i, j))
        minHeap = edges[:]
        heapq.heapify(minHeap)
        mst = []
        total = 0
        while len(mst) < n - 1:
            dist, n1, n2 = heapq.heappop(minHeap)
            if dsu.union(n1, n2):
                total += dist
                mst.append((dist, n1, n2))
    


        return total





class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
    
    def find(self, v):
        if v != self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union(self, v1, v2):
        p1 = self.find(v1)
        p2 = self.find(v2)

        if p1 == p2:
            return False
        
        if self.rank[p1] >= self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True
