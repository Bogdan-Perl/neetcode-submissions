class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        sumArr = []
        total = 0
        for num in nums:
            total += num
            sumArr.append(total)

        predVals = {}

        for elm in sumArr: #1, 0, 0
            target = elm - k
            if target == 0:
                res += predVals.get(0, 0) + 1

            elif target in predVals:
                res += predVals[target]
            predVals[elm] = predVals.get(elm, 0) + 1

        return res