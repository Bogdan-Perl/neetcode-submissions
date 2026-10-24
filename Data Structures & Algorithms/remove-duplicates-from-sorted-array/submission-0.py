class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        L = 0
        if len(nums) == 1:
            return 1
        while L < len(nums):
            while L + 1 < len(nums) and nums[L+1] == nums[L]:
                nums.pop(L+1)
                k+=1
            L += 1
        return len(nums)
