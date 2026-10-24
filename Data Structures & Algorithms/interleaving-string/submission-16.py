class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N, M, P = len(s1), len(s2), len(s1) + len(s2)
        if len(s3) != N + M: 
            return False

        dp = [[False]*(N+1) for _ in range(M+1)]
        dp[M][N] = True

        for j in range(M, -1, -1):
            for i in range(N, -1, -1):
                k = i + j
                if i < N and s1[i] == s3[k] and dp[j][i+1]:
                    dp[j][i] = True
                if j < M and s2[j] == s3[k] and dp[j + 1][i]:
                    dp[j][i] = True

        return dp[0][0]