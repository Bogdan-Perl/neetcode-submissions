class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        x = sorted(nums, reverse=True)
        return x[k -1]