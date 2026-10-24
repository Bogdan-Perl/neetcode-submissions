class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        cache = {}

        def memoization(r, c):
            if r == ROWS or c == COLS:
                return 0
            if r == ROWS-1 and c==COLS-1:
                return 1
            if (r,c) in cache:
                return cache[(r,c)]

            cache[(r,c)] = memoization(r+1, c) + memoization(r, c+1)
            return cache[(r,c)]
        return memoization(0, 0)
            
            
            