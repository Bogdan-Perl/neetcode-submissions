class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i : set() for i in range(9)}
        cols = {i : set() for i in range(9)}
        def travBox(r, c):
            subBox = set()
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    cell = board[i][j]
                    if cell == ".":
                        continue
                    if (cell in rows[i] or cell in cols[j]
                        or cell in subBox):
                        return False
                    rows[i].add(cell)
                    cols[j].add(cell)
                    subBox.add(cell)
            return True
        
        for r in range(0, 8, 3):
            for c in range(0, 8, 3):
                if not travBox(r, c):
                    return False
        return True





