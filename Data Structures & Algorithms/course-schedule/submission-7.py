class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjList = defaultdict(list)

        for crs, pre in prerequisites:
            adjList[pre].append(crs) 

        def dfs(crs, path, visted):
            if crs in path:
                return False
            if crs in visted:
                return True
            
            visted.add(crs)

            path.add(crs)
            for nxt in adjList[crs]:
                if not dfs(nxt, path, visted):
                    return False
            path.remove(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs, set(), set()):
                return False
        
        return True




        
