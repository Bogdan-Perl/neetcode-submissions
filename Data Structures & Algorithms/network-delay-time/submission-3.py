class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = [float('inf')] * (n+1)

        dist[k] = 0
        heap = [(0, k)]
        while heap:
            curr_dist, u = heapq.heappop(heap)
            if dist[u] < curr_dist:
                continue
            
            for v, w in graph[u]:
                new_dist = curr_dist + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))


        return max(dist[1:]) if max(dist[1:]) != float('inf') else -1
