class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def memo(i, j):
            if j == len(t):
                return 1
            if i == len(s): 
                return 0

            if s[i] == t[j]:
                return memo(i + 1, j + 1) + memo(i + 1, j)
            else:
                return memo(i + 1, j)
        

        return memo(0, 0)