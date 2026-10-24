class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L = 0
        length = float('-inf')

        for R in range(len(s)):
            while s[R] in window:
                if s[L] == s[R] or s[L] in window:
                    window.remove(s[L])
                L += 1

            window.add(s[R])
            length = max(length, R-L+1)
            
        return length if length != float('-inf') else 0