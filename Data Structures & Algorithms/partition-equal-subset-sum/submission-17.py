class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2

        memo = {} 

        def dp(idx, total):
            if (idx, total) in memo:
                return memo[(idx, total)]
            if idx == len(nums):
                return False
            if total == target:
                return True
            memo[(idx, total)] = dp(idx + 1, total) or dp(idx + 1, total + nums[idx])
            return memo[(idx, total)]
        
        return dp( 0, 0)


