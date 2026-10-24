class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars = collections.Counter(s1)
        if len(s2) < len(s1):
            return False
        
        curr = Counter()
        L = 0
        for R in range(len(s2)):
            curr[s2[R]] += 1
            if R - L + 1 > len(s1):
                curr[s2[L]] -= 1
                L += 1

            if R - L + 1 == len(s1) and curr == chars:
                return True

        return False
            

                
            

