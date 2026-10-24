class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)


        def find(v):
            if par[v] == v:
                return v
            else:
                par[v] = find(par[v])
            return par[v]

        def union(v1, v2):
            p1, p2 = find(v1), find(v2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p1] < rank[p2]:
                par[p1] = p2
            else:
                rank[p1] += 1
                par[p2] = p1
            return True

        for v1, v2 in edges:
            if not union(v1, v2):
                return [v1, v2]
        return []