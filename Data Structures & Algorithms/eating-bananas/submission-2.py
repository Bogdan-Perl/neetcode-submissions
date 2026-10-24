class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)

        while L <= R:
            k = L + (R - L)//2

            if self.traverse(piles, h, k) and ((k > 1 and not self.traverse(piles, h, k-1)) or k==1):
                return k
            elif self.traverse(piles, h, k):
                R = k - 1
            else:
                L = k + 1





        '''
        The maximum eating length is max of the array
        min is 1

        '''
    def traverse(self, piles, h, k):
        counter = 0
        for pile in piles:
            counter += -(-pile//k)
        
        if counter > h:
            return 0
        elif counter <= h:
            return 1
        