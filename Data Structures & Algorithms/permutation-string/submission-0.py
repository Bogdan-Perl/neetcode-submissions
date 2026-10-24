from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars = Counter(s1)
        if len(s2) < len(s1):
            return False

        curr = defaultdict(int)
        L = 0
        for R in range(len(s2)):
            curr[s2[R]] += 1

            if R - L + 1 > len(s1):
                left_ch = s2[L]
                curr[left_ch] -= 1
                if curr[left_ch] == 0:
                    del curr[left_ch]      # 🔴 important
                L += 1

            if R - L + 1 == len(s1) and curr == chars:
                return True

        return False
