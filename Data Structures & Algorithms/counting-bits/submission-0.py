class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(self.hammingWeight(i))
        return res

    def hammingWeight(self, n: int) -> int:
        counter = 0
        while n > 0:
            counter += 1 if n & 1 else 0
            n >>= 1
        return counter
        