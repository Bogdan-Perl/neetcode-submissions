class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        curr_dp = [1] + [0] * (amount)
        for c in coins:
            for a in range(c, amount + 1):
                    curr_dp[a] += curr_dp[a - c]
        return curr_dp[amount]