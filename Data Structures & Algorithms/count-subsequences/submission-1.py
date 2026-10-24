class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def memo(i, j):
            if j == len(t):
                return 1
            if i == len(s): 
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            nxt = memo(i + 1, j)
            if s[i] == t[j]:
                nxt += memo(i + 1, j + 1)
            dp[(i, j)] = nxt
            return dp[(i, j)]

        return memo(0, 0)