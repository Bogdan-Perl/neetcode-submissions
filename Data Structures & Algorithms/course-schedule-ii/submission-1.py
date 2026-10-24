class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        topSort = []

        for crs, pre in prerequisites:
            g[pre].append(crs)


        def dfs(crs, visted, path):
            if crs in path:
                return False
            if crs in visted:
                return True
            
            path.add(crs)
            visted.add(crs)

            for nxt in g[crs]:
                if not dfs(nxt, visted, path):
                    return False
            path.remove(crs)
            topSort.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs, set(), set()):
                return []

        topSort.reverse()
        return topSort
