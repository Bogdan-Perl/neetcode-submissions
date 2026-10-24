class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum = 0
        maxsum = float('-inf')

        for n in nums:
            currsum = max(0, currsum) + n 
            maxsum = max(currsum, maxsum)

        return maxsum

        