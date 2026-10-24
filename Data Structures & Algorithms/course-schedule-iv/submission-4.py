class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        g = defaultdict(list)
        crsToPre = defaultdict(list)

        for pre, crs in prerequisites:
            g[pre].append(crs)
        


        def dfs(crs):
            if crs in crsToPre:
                return crsToPre[crs]

            
            reachable = set()
            for nxt in g[crs]:
                reachable.add(nxt)
                reachable |= dfs(nxt)
            crsToPre[crs] = reachable
            return reachable

        for crs in range(numCourses):
            dfs(crs)
        res = []
        for pre, crs in queries:
            res.append(crs in crsToPre[pre])
        
        return res




