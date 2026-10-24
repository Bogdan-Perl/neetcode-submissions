class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)/2
        cache = {}

        def memoization(curr, i):
            if curr == 0:
                return True
            if curr < 0 or i >= len(nums):
                return False
            
            #skip
            return memoization(curr, i + 1) or memoization(curr - nums[i], i + 1)


        return memoization(target, 0)
