class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [0 <- 1]
        def dfs(adj, src, path, vist):
            if src in path:
                return False
            if src in vist:
                return True
            path.add(src)
            vist.add(src)
            for dst in adj[src]:
                if not dfs(adj, dst, path, vist):
                    return False
            path.remove(src)
            
            return True

        adj = defaultdict(list)
        topSort = []
        vist = set()
        path = set()


        for dst, src in prerequisites:
            adj[src].append(dst)
        
        for i in range(numCourses):
            if not dfs(adj, i, path, vist):
                return False
        
        return True


        

        

