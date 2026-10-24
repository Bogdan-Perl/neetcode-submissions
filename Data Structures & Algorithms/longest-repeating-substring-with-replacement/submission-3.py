class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = {}
        length = 0
        L = 0
        maxf = 0

        for R in range(len(s)):
            frequencies[s[R]] = 1 + frequencies.get(s[R], 0)
            maxf = max(maxf, frequencies[s[R]])

            while (R - L + 1) - maxf > k:
                frequencies[s[L]] -= 1
                L += 1
            length = max(length, R - L + 1)

        return length




                

        