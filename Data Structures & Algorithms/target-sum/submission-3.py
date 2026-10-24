class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(idx, curr):
            if idx == len(nums):
                return 1 if curr == target else 0
            if (idx, curr) in memo:
                return memo[(idx, curr)]

            sub = add = 0

            sub += dp(idx + 1, curr + nums[idx])

            add += dp(idx + 1, curr - nums[idx])
            memo[(idx, curr)] = sub + add
            return memo[(idx, curr)]
        
        return dp(0, 0)


