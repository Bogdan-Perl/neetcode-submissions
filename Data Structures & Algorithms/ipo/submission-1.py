class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCapital)
        maxProfits = []

        for i in range(k):
            while minCapital and minCapital[0][0] <= w:
                x = heapq.heappop(minCapital)[1]
                heapq.heappush(maxProfits, -x)
            if not maxProfits:
                break
            maxProfit = -heapq.heappop(maxProfits)
            w += maxProfit

        return w