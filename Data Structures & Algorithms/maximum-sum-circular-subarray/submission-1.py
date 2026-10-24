class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
            minSum = maxSum = nums[0]
            currMin = currMax = 0
            total = 0
            for num in nums:
                total+=num
                currMax = max(currMax + num, num) 
                currMin = min(currMin + num, num)
                maxSum = max(maxSum, currMax)
                minSum = min(minSum, currMin)
            
            return max(maxSum, total - minSum) if maxSum > 0 else maxSum