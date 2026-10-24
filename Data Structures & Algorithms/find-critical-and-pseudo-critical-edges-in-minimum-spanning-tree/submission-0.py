class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, v):
        while v != self.par[v]:
            self.par[v] = self.par[self.par[v]]
            v = self.par[v]
        return v

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)

        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        e = []
        for i, edge in enumerate(edges):
            e.append([i] + edge)

        e.sort(key=lambda x:x[3])
        mst = 0
        total_mst = 0
        dsu = UnionFind(n)
        critical, pseudo = [], []

        for i, n1, n2, w in e:
            if dsu.union(n1, n2):
                total_mst += w
        

        for i, n1, n2, w in e:
            dsu = UnionFind(n)
            total = 0
            for j, v1, v2, wei in e:
                if i != j and dsu.union(v1, v2):
                    total += wei
            

            if max(dsu.rank) != n or total > total_mst:
                critical.append(i)
                continue
            

            dsu = UnionFind(n)
            dsu.union(n1, n2)
            total = w
            for j, v1, v2, wei in e:
                if dsu.union(v1, v2):
                    total += wei
            if total == total_mst:
                pseudo.append(i)
        
        return [critical, pseudo]






        





















