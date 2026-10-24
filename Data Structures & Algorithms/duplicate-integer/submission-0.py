class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDuplicates = set(nums)
        return len(nums) != len(noDuplicates)
         