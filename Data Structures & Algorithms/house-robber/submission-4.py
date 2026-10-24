class Solution:
    def rob(self, nums: List[int]) -> int:
        memoize = {} # i : max money
        def dfs(i):
            if i > len(nums) - 1:
                return 0
            if i in memoize:
                return memoize[i]
            memoize[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return memoize[i]
        return dfs(0)