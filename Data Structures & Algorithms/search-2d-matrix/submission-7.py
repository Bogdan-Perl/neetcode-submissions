class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1

        row = 0
        while top <= bottom:
            row = top + (bottom-top)//2
            if matrix[row][-1] < target:
                top += 1
            elif matrix[row][0] > target:
                bottom -= 1
            else:
                break
        if not top <= bottom:
            return False
        
        L, R = 0, columns - 1
        while L <= R:
            column = L + (R-L)//2
            if matrix[row][column] < target:
                L = column + 1
            elif matrix[row][column] > target:
                R = column - 1
            else:
                return True
        return False
