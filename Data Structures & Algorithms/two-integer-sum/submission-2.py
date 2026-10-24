class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictV = {i : (target - nums[i]) for i in range(len(nums))}

        for i in range(len(nums)):
            for v in range(i+1, len(dictV)):
                if nums[i] == dictV[v]:
                    return [i,v]

