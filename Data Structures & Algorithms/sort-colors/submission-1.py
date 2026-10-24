class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 0, 0]
        for num in nums:
            colors[num] += 1
        
        i = 0
        for color, amount in enumerate(colors):
            for _ in range(amount):
                nums[i] = color
                i += 1