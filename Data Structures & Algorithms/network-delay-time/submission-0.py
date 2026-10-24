class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))            
        
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        # (distance, node)
        heap = [(0, k)]

        while heap:
            curr_dist, u = heapq.heappop(heap)

            if curr_dist > dist[u]:
                continue
                
            for v, weight in graph[u]:
                new_dist = curr_dist + weight
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))

        res = max(dist[1:])
        return res if res != float('inf') else -1


