class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        g = defaultdict(set)
        crsToPre = defaultdict(set)
        state = [0] * numCourses
        # 0 -> unvisted, 1 -> visting, 2 ->visted

        for pre, crs in prerequisites:
            g[pre].add(crs)
        topSort = []
        has_cycle = False
        def dfs(u):
            nonlocal has_cycle
            if state[u] == 1:
                has_cycle = True
                return
            
            if state[u] == 2:
                return

            state[u] = 1
            for v in g[u]:
                dfs(v)
            state[u] = 2
            topSort.append(u)

        for i in range(numCourses):
            if state[i] == 0:
                dfs(i)

        topSort.reverse()
        if has_cycle:
            return []
        res = []
        crsForPre = defaultdict(set)
        for u in topSort:
            for v in g[u]:
                crsForPre[v].add(u)
                crsForPre[v].update(crsForPre[u])
        
        return [u in crsForPre[v] for u,v in queries]




        
        return [u in crsToPre[v] for u, v in queries]




