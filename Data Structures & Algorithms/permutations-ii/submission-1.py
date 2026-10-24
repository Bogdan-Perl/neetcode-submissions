class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = collections.Counter(nums)

        def dfs():
            if len(perm) == len(nums):
                res.append(perm[::])
            for c in count:
                if count[c] > 0:
                    count[c] -= 1
                    perm.append(c)

                    dfs()

                    count[c] += 1
                    perm.pop()
        dfs()
        return res

