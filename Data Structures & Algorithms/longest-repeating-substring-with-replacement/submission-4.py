class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {0 : 0}
        L = 0
        length = 0
        for R in range(len(s)):
            chars[s[R]] = chars.get(s[R], 0) + 1
            while R-L+1 - max(chars.values()) > k:
                chars[s[L]] -= 1 
                if chars[s[L]] == 0:
                    del chars[s[L]]
                L += 1
            length = max(length, R-L+1)
        
        return length