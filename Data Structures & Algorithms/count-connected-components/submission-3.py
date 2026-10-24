class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        vist = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bfs(node):
            q = deque([node])
            vist[node] = True
            while q:
                curr = q.popleft()
                for nei in adj[curr]:
                    if not vist[nei]:
                        vist[nei] = True
                        q.append(nei)
            
        res = 0
        for node in range(n):
            if not vist[node]:
                vist[node] = True
                bfs(node)
                res +=1
        return res