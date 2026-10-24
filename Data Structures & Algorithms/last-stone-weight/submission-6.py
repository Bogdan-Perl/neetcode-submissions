class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            lstone = heapq.heappop(heap)
            rstone = heapq.heappop(heap)
            res = lstone - rstone
            if res != 0:
                heapq.heappush(heap, res)
        if heap:
            return abs(heap[0])
        return 0




