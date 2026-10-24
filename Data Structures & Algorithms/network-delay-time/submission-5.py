class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = [(0, k)]
        adjList = defaultdict(list)
        minTimes = [float('inf')] *(n+1)
        minTimes[k] = 0
        for u, v, t in times:
            adjList[u].append((t, v))
        
        
        while minHeap:
            curr_t, u = heapq.heappop(minHeap)
            if curr_t > minTimes[u]:
                continue
            
            for nxt_t, v in adjList[u]:
                new_t = curr_t + nxt_t
                if new_t < minTimes[v]:
                    minTimes[v] = new_t
                    heapq.heappush(minHeap, (new_t, v))

            

        return max(minTimes[1:]) if max(minTimes[1:]) != float('inf') else -1