class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[ROWS-1][COLS-1]:
            return 0
        prevRow = [0 if i != COLS-1 else 1 for i in range(COLS)]

        # paths to cell r,c is equal to 
        # the sum of paths to cell r+1,c and cell r,c+1
        for r in range(ROWS-1, -1, -1):
            currRow = [0] * COLS
            if (not obstacleGrid[r][COLS-1]
            and prevRow[COLS-1]) : currRow[COLS-1] = 1

            for c in range(COLS-2, -1, -1):
                if not obstacleGrid[r][c]:
                    currRow[c] = currRow[c+1] + prevRow[c]
                else:
                    currRow[c] = 0
            prevRow = currRow
        
        return prevRow[0]




