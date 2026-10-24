class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        maxDay = days[-1]
        travel = set(days)
        dp = [float('inf')] * (maxDay + 1)
        dp[0] = 0

        for d in range(1, maxDay + 1):
            curr_dp = dp[:]

            if d not in travel:
                curr_dp[d] = dp[d-1]
            else:
                o = dp[max(0, d-1)] + costs[0]
                w = dp[max(0, d-7)] + costs[1]
                m = dp[max(0, d-30)] + costs[2]

                curr_dp[d] = min(o, w, m)

            dp = curr_dp
        return dp[maxDay]
