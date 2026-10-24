class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        memo = {}

        def topdown(i, j):
            state = (i, j)
            if i == len(word1):
                return len(word2) - j
            elif j == len(word2):
                return len(word1) - i
            elif state in memo:
                return memo[state]
            
            if word1[i] == word2[j]:
                memo[state] = topdown(i + 1, j + 1)
            else:
                memo[state] = 1 + min(topdown(i + 1, j), topdown(i, j + 1), topdown(i + 1, j + 1))
            
            return memo[state]
        return topdown(0,0)