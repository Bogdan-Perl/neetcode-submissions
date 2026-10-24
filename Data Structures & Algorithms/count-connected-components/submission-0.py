class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        def find(v):
            while v != par[v]:
                par[v] = par[par[v]]
                v = par[v]
            return v
        def union(v1, v2):
            p1, p2 = find(v1), find(v2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return True

        res = n
        for v1, v2 in edges:
            if union(v1, v2):
                res -=1
        return res
            








        return res