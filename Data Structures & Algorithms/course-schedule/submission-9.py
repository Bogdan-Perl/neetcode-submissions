class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        top = []
        adjList = defaultdict(list)
        for crs, pre in prerequisites:
            adjList[pre].append(crs)

        def dfs(crs, path, vist):
            if crs in path:
                return False
            if crs in vist:
                return True
            vist.add(crs)
            path.add(crs)

            for nxt in adjList[crs]:
                if not dfs(nxt, path, vist):
                    return False
            path.remove(crs)
            top.append(crs)
            return True


        for crs in range(numCourses):
            if not dfs(crs, set(), set()):
                return False

        top.reverse() #IK not required but is final top right?
        return True



