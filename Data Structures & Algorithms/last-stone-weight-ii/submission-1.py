class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2

        dp = [0] * (target + 1)

        for w in stones:
            curr_dp = dp[:]
            for t in range(target+1):
                curr_dp[t] = dp[t]
                if w <= t:
                    curr_dp[t] = max(dp[t], dp[t-w] + w)
            dp = curr_dp




        return abs(total - 2*dp[target])