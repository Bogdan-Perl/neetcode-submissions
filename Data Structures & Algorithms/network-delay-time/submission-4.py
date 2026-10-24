class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = []
        adjList = defaultdict(list)
        minTimes = [float('inf') for i in range(n+1)]
        minTimes[k] = 0
        for u, v, t in times:
            adjList[u].append((t, v))
        for t, v in adjList[k]:
            heapq.heappush(minHeap, (t, k, v)) 
        
        while minHeap:
            t, u, v  = heapq.heappop(minHeap)
            new_time = minTimes[u] + t
            if minTimes[v] < new_time:
                continue
            minTimes[v] = new_time
            for t2, v2 in adjList[v]:
                heapq.heappush(minHeap, (t2, v, v2))

        return max(minTimes[1:]) if max(minTimes[1:]) != float('inf') else -1