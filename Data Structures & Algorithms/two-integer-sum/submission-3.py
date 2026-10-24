class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}

        for idx, val in enumerate(nums):
            if val in x:
                return [x[val], idx]
            else:
                x[target - val] = idx
        
        return -1