class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        maxHeight = 0
        while L < R:
            maxHeight = max(maxHeight, (R-L)*min(height[L],height[R]))
            if height[L] < height[R]:
                L+=1
            else:
                R -= 1
        
        return maxHeight