class Solution:
    def trap(self, height: List[int]) -> int:
        leftTall = [0] * len(height)
        rightTall = [0] * len(height)
        lMax = 0
        rMax = 0
        totalWater = 0
        for i in range(len(height)):
            if height[i] > lMax:
                lMax = height[i]
            leftTall[i] = lMax

            if height[-i-1] > rMax:
                rMax = height[-i-1]
            rightTall[-i-1] = rMax
        
        for idx, ht in enumerate(height):
            water = min(leftTall[idx], rightTall[idx]) - ht
            totalWater += water if water > 0 else 0
        
        return totalWater
            
