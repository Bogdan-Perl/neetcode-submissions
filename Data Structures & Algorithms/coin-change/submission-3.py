class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for v in coins:
            curr_dp = dp[:]
            for amt in range(amount + 1):
                exclude = dp[amt]
                include = float('inf')
                if amt >= v:
                    include = curr_dp[amt-v] + 1
                curr_dp[amt] = min(include, exclude)
                    

            dp = curr_dp




        return dp[amount] if dp[amount] != float('inf') else -1