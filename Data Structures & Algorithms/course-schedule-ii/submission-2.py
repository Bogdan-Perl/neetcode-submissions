class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        topSort = []
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            indegree[crs] += 1
            g[pre].append(crs)

        q = deque()
        for crs in range(numCourses):
            if not indegree[crs]:
                q.append(crs)
        
        while q:
            crs = q.popleft()
            topSort.append(crs)

            for nxt in g[crs]:
                indegree[nxt] -= 1
                if not indegree[nxt]:
                    q.append(nxt)

        return topSort if len(topSort) == numCourses else []

