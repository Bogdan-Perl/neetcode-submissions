class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        while L < R:
            # If the window is already sorted, the min is at L
            if nums[L] < nums[R]:
                return nums[L]
            M = (L + R) // 2
            # Left half [L..M] is sorted; min must be to the right of M
            if nums[M] >= nums[L]:
                L = M + 1
            else:
                # Rotation (and min) lies in [L..M]
                R = M
        return nums[L]
