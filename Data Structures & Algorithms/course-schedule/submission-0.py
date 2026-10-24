class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        visted = set()
        def dfs(crs):
            if crs in visted:
                return False
            if adjList[crs] == []:
                return True
            
            visted.add(crs)
            for nei in adjList[crs]:
                if not dfs(nei): return False
            visted.remove(crs)
            adjList[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True