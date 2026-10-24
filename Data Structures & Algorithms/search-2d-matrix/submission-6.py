class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, w = len(matrix), len(matrix[0])
        r, c = 0, w - 1

        while c >= 0 and r < l:
            if matrix[r][c] < target:
                r += 1
            elif matrix[r][c] > target:
                c -= 1
            else: 
                return True
        return False