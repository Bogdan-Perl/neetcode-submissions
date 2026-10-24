class Solution:
    def binarySearch(self, nums, L, R, target):
        if L > R:
            return -1
        mid = L + ((R-L) // 2)
        if nums[mid] < target:
            return self.binarySearch(nums, mid + 1, R, target)
        elif nums[mid] > target:
            return self.binarySearch(nums, L, mid -1 , target)
        else:
            return mid

    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        return self.binarySearch(nums, L, R, target)

