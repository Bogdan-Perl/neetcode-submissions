class Solution:
    def climbStairs(self, n: int) -> int:
        #recursive relation is paths to step i is 
        #equal to paths to step i-1 plus paths to step i-2
        if n <= 2:
            return n
        tab = [1, 2]

        for i in range(n-2):
            temp = tab[1]
            tab[1] = sum(tab)
            tab[0] = temp
            

        return tab[1]
