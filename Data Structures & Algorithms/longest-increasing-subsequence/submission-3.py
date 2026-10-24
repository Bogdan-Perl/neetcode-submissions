class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dfs(p, c):

            if c == len(nums):
                return 0
            if (p, c) in memo:
                return memo[(p,c)]
            
            LIS = dfs(p, c+1)
            if p == -1 or nums[p] < nums[c]:
                LIS = max(LIS, 1 + dfs(c, c+1))
                memo[(p, c)] = LIS

            return LIS
        return dfs(-1, 0)