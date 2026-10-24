class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i, currCombo):
            if len(currCombo) == k:
                res.append(currCombo[::])
                return 
            if i > n:
                return
            for j in range(i, n+1): 
                currCombo.append(j)
                backtrack(j+1, currCombo)
                currCombo.pop()

        backtrack(1, [])
        return res