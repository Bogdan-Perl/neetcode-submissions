class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #recursive relation, paths (m,n) = paths to (m+1) + paths (n+1)
        prevRow = [0 if i != n-1 else 0 for i in range(n)]*n

        for r in range(m-1, -1, -1):
            currRow = [0]*n
            currRow[n-1] = 1

            for c in range(n-2, -1, -1):
                currRow[c] = currRow[c+1] + prevRow[c]
            prevRow = currRow
        return prevRow[0]


