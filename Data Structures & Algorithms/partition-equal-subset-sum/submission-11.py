class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        if total % 2:
            return False
        target = total // 2

        dp = [False] * (target + 1)
        nxtDp = [False] * (target + 1)

        dp[0] = True



        for i in range(n):
            for j in range(1, target + 1):
                if nums[i] <= j:
                    nxtDp[j] = dp[j] or dp[j - nums[i]]
                else:
                    nxtDp[j] = dp[j] 
            dp = nxtDp
            nxtDp = [False] * (target + 1)
            nxtDp[0] = True

                
        
        return dp[target]
                


                