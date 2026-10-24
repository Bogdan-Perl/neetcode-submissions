class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = UnionFind(n)
        edges = []
        minHeap = []
        mst = []
        total = 0

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))

        for weight, n1, n2 in edges:
            heapq.heappush(minHeap, [weight, n1, n2])
        
        while len(mst) < n - 1:
            weight, n1, n2 = heapq.heappop(minHeap)
            if not dsu.union(n1, n2):   continue
            total += weight
            mst.append([n1, n2])
        return total
            





class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [1] * (n + 1)

    def find(self, v):
        if v != self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


    

        