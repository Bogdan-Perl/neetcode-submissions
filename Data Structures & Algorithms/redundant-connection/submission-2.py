class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visted = [False] * (n+1)
        cycle = set()
        startCycle = -1

        def dfs(curr, par):
            nonlocal startCycle
            if visted[curr]:
                startCycle = curr
                return True
            visted[curr] = True
            for nei in adj[curr]:
                if nei == par:
                    continue
                if dfs(nei, curr):
                    if startCycle != -1:
                        cycle.add(curr)
                    if curr == startCycle:
                        startCycle = -1
                    return True
            visted[curr] = False
            return False
        dfs(1, -1)
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]
        return []
        


                

