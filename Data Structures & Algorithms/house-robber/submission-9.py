class Solution:
    def rob(self, nums: List[int]) -> int:
        #the max money for position i is the max of position 
        # of i-2 and i-3
        # nums[i] = max(nums[i-2], nums[i-3])

        if len(nums) <= 2:
            return max(nums)
        maxMoney = [0] + nums
        maxMoney[1], maxMoney[2] = nums[0], nums[1]

        for i in range(3, len(maxMoney)):
            maxMoney[i] = nums[i-1] + max(maxMoney[i-2], maxMoney[i-3])
        
        return max(maxMoney[-1], maxMoney[-2])


