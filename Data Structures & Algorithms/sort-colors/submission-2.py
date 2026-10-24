class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums)

        idx = 0 
        for i in range(3):
            while count[i]:
                nums[idx] = i
                idx += 1
                count[i] -= 1
        
