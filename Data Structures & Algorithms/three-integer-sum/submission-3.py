class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
#len = 3, 0 - 2, p1 = 0, p2 = 1, p3 = 2
        for p1 in range(len(nums)-2):
            if p1 > 0 and nums[p1] == nums[p1-1]:
                continue
            p2 = p1 + 1
            p3 = len(nums)-1
            while p2 < p3:
                curr = nums[p1] + nums[p2] + nums[p3]
                if curr == 0:
                    res.append([nums[p1], nums[p2], nums[p3]])
                    p2 += 1
                    while nums[p2] == nums[p2-1] and p2 < p3:
                        p2 += 1

                elif curr > 0:
                    p3-=1
                else:
                    p2+=1
                     
        return res
                

