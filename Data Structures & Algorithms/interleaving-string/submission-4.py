class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        if len(s3) != len(s1) + len(s2):
            return False

        def topdown(i, j):
            state = (i, j)
            k = i + j
            if k == len(s3):
                return True
            if state in memo:
                return memo[state]


            side1 = False
            side2 = False
            if i < len(s1) and s1[i] == s3[k]:
                side1 = topdown(i + 1, j)
            if j < len(s2) and s2[j] == s3[k]:
                side2 = topdown(i, j + 1)
            memo[state] = side1 or side2
            return memo[state]

        if not (s1 or s2 or s3): return True
        return topdown(0, 0)  