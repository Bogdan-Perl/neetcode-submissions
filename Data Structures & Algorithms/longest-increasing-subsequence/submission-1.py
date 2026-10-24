class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(p, c):
            if c == len(nums):
                return 0
            
            LIS = dfs(p, c+1)
            if p == -1 or nums[p] < nums[c]:
                LIS = max(LIS, 1 + dfs(c, c+1))

            return LIS
        return dfs(-1, 0)