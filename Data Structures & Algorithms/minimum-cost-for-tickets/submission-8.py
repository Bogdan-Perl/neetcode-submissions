class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        maxDay = days[-1]
        travel = set(days)
        curr_dp = [float('inf')] * (maxDay + 1)
        curr_dp[0] = 0

        for d in range(1, maxDay + 1):

            if d not in travel:
                curr_dp[d] = curr_dp[d-1]
            else:
                o = curr_dp[max(0, d-1)] + costs[0]
                w = curr_dp[max(0, d-7)] + costs[1]
                m = curr_dp[max(0, d-30)] + costs[2]

                curr_dp[d] = min(o, w, m)

        return curr_dp[maxDay]
