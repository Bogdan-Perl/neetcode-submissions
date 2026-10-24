class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def memoization(n):
            if n==0:
                return 1
            if n < 0:
                return 0
            if n in cache:
                return cache[n]
            res = self.climbStairs(n-1) + self.climbStairs(n-2)
            cache[n] = res
            return cache[n]
        

        return memoization(n)