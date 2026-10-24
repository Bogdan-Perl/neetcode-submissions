class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        curr_dp = [0] * (amount + 1)
        curr_dp[0] = 1
        for c in coins:
            for a in range(1, amount + 1):
                if a >= c :
                    curr_dp[a] += curr_dp[a - c]
        return curr_dp[amount]