class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []
        def backtrack(i, curr):
            if sum(curr) == target:
                if curr in combos:
                    return
                combos.append(curr[::])
                return
            if sum(curr) > target or i >= len(nums):
                return
            
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()

            curr.append(nums[i])
            backtrack(i, curr)
            curr.pop()

            backtrack(i + 1, curr)
        backtrack(0, [])
        return combos

            # (Curr Number)
            # we can eaither:
            # add curr number and iterate
            # add curr number and not iterate
            # not add curr number and iterate
            