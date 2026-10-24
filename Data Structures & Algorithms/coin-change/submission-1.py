class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            curr_dp = [float('inf')] * (amount + 1)

            for i in range(amount + 1): 
                skip = dp[i]
                include = float('inf')
                if i >= coin:
                    include = curr_dp[i - coin] + 1
                curr_dp[i] = min(include, skip)
            dp = curr_dp


        return dp[amount] if dp[amount] != float('inf') else -1

