class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) -1 

        while L < R:
            if nums[L] < nums[R]:
                return nums[L]
            
            M = (L + R) //2
            if nums[L] <= nums[M]:
                L = M + 1
            else:
                R = M 
        return nums[L]
