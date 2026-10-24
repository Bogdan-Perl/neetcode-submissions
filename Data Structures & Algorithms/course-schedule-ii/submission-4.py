class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        g = defaultdict(list)
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            g[pre].append(crs)
            indegree[crs] += 1
        
        q = deque()
        topSort = []

        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)
            
        
        while q:
            crs = q.popleft()

            for nei in g[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            topSort.append(crs)
        

        return topSort if len(topSort) == numCourses else []
