class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        res = R

        while L <= R:
            k = (L + R) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            if hours <= h:
                res = min(res, k)
                R = k - 1
            else:
                L = k + 1
        return res