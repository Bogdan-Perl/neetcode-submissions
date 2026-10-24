class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text1) + 1)

        for i in range(len(text2)):
            curr_dp = dp[:]
            for j in range(len(text1)):
                if text1[j] == text2[i]:
                    curr_dp[j + 1] = 1 + dp[j]
                else:
                    curr_dp[j + 1] = max(dp[j + 1], curr_dp[j])
            dp = curr_dp
        return dp[len(text1)]