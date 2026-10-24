class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mNum = nums[0]
        count = 0
        for num in nums:
            if num == mNum:
                count +=1
            else:
                count -=1 
            if count < 0:
                mNum = num 
                count = 0
        return mNum
        