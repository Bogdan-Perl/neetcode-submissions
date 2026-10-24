class Solution:
    cache = {}
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 1
        if n < 0:
            return 0
        if n in self.cache:
            return self.cache[n]
        res = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.cache[n] = res
        return self.cache[n]
        

        return climbStairs(n)