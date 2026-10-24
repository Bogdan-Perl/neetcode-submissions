class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(idx, curr):
            if idx == len(nums):
                if curr == target:
                    return 1
                else:
                    return 0

            sub = add = 0

            sub += dp(idx + 1, curr + nums[idx])

            add += dp(idx + 1, curr - nums[idx])

            return sub + add
        
        return dp(0, 0)


