class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        preProduct = 1
        postfix = []
        postProduct = 1

        R = len(nums) - 1
        for L in range(len(nums)):
            preProduct *= nums[L]
            postProduct *= nums[R]
            R-= 1

            prefix.append(preProduct)
            postfix.append(postProduct)

        
        res = []
        for idx, num in enumerate(nums):
            if idx == 0:
                curr = postfix[len(nums)-1-idx-1]
            elif idx == len(nums)-1:
                curr = prefix[idx-1]
            else:
                curr = prefix[idx-1] * postfix[len(nums)-1-idx-1]
            res.append(curr)
        return res