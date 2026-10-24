class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = [0] * numCourses
        adjList = defaultdict(list)

        for crs, pre in prerequisites:
            indegree[crs] += 1
            adjList[pre].append(crs) # Prereq : what comes after
        
        q = deque()
        for crs in range(numCourses):
            if indegree[crs] == 0: #indegree[crs] == 0
                q.append(crs)
        
        top = []

        while q:
            curr = q.popleft()
            top.append(curr)

            for nxt in adjList[curr]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        return len(top) == numCourses


        
