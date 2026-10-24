class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        g = defaultdict(set)
        crsToPre = defaultdict(set)

        for pre, crs in prerequisites:
            g[pre].add(crs)
        


        def dfs(crs):
            if crs in crsToPre:
                return crsToPre[crs]

            
            for nxt in g[crs]:
                crsToPre[crs].add(nxt)
                crsToPre[crs] |= dfs(nxt)
            return crsToPre[crs]

        for crs in range(numCourses):
            dfs(crs)
        res = []
        for pre, crs in queries:
            res.append(crs in crsToPre[pre])
        
        return res




