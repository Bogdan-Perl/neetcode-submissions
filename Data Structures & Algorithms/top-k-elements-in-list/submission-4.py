class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        ordered = sorted(count.items(), key = lambda x : -x[1])
        return [ordered[i][0] for i in range(k)]