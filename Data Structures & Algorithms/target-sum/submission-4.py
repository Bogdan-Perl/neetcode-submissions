class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # item -> {sums : count}
        
        dp = defaultdict(int)
        dp[0] = 1
        
        for i in range(len(nums)):
            newDp = defaultdict(int)
            for total, count in dp.items():
                newDp[total + nums[i]] += count
                newDp[total - nums[i]] += count
            dp = newDp

        return dp[target]



