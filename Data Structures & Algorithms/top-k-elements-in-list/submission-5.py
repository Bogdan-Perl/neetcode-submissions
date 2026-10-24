class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for num, c in count.items():
            freq[c].append(num)
        
        for i in range(len(nums), 0, -1):
            if k == 0:      break
            for j in range(len(freq[i])):
                k -= 1
                res.append(freq[i][j])
        return res
