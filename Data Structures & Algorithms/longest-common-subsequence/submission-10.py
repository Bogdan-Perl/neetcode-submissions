class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = {} # state : lcs

        def topdown(i, j):
            state = (i, j)
            if i == len(text1) or j == len(text2):
                return 0 
            if state in memo:
                return memo[state]
            
            if text1[i] == text2[j]:
                memo[state] =  1 + topdown(i + 1, j + 1)
            else:
                memo[state] = max(topdown(i + 1, j), topdown(i, j + 1))
            return memo[state]
        return topdown(0, 0)
            