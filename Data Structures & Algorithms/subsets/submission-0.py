class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, curr = [], []
        self.helper(nums, subsets, curr, 0)
        return subsets
        
    def helper(self, nums, subsets, curr, i):
        if i == len(nums):
            subsets.append(curr.copy())
            return
        
        curr.append(nums[i])
        self.helper(nums, subsets, curr, i + 1)
        curr.pop()
        
        self.helper(nums, subsets, curr, i + 1)



