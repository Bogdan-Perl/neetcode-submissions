class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        g = defaultdict(set)
        crsToPre = defaultdict(set)
        indegree = [0] * numCourses

        for pre, crs in prerequisites:
            indegree[crs] += 1
            g[pre].add(crs)
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])


        while q:
            crs = q.popleft()
            for nxt in g[crs]:
                crsToPre[nxt].add(crs)
                crsToPre[nxt].update(crsToPre[crs])
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)


        return [u in crsToPre[v] for u, v in queries]




