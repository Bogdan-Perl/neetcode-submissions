class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memoize = {}

        def topdowndp(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) in memoize:
                return memoize[(i, j)]
            if word1[i] == word2[j]:
                return topdowndp(i + 1, j + 1)
            else:
                memoize[(i, j)] = min(topdowndp(i + 1, j), topdowndp(i, j + 1), topdowndp(i + 1, j + 1)) + 1
                return memoize[(i, j)]
        return topdowndp(0, 0)

