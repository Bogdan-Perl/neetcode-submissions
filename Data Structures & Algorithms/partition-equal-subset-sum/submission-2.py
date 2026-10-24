class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)/2
        cache = {}

        def memoization(curr, i):
            if (curr, i) in cache:
                return cache[(curr, i)]
            if curr == 0:
                return True
            if curr < 0 or i >= len(nums):
                return False
            
            res =  memoization(curr, i + 1) or memoization(curr - nums[i], i + 1)
            cache[(curr, i)] = res

            
            return res


        return memoization(target, 0)
