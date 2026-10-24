class Solution:
    def climbStairs(self, n: int) -> int:
        #recursive relation is paths to step i is 
        #equal to paths to step i-1 plus paths to step i-2
        if n <= 2:
            return n
        tab = [0]* (n+1)

        tab[1], tab[2] = 1, 2

        for i in range(3, n+1):
            tab[i] = tab[i-1] + tab[i-2]

        return tab[n]
