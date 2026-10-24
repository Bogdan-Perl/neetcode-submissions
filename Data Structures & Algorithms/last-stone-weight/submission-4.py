class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            lstone = abs(heapq.heappop(heap))
            rstone = abs(heapq.heappop(heap))
            res = abs(lstone - rstone)
            if res != 0:
                heapq.heappush(heap, -res)
        if heap:
            return abs(heap[0])
        return 0




