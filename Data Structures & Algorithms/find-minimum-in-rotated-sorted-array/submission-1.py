class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        res = nums[0]
        while L<=R:
            if nums[L] < nums[R]:
                res = min(res, nums[L])
                break
            M = (R+L) // 2
            res = min(res, nums[M])
            #Input: nums = [6,1,2,4,5]
            if nums[M] >= nums[L]:
                L = M + 1
            else:
                R = M - 1
        
        return res