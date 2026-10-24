class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        L = 0
        length = 0

        for R in range(len(s)):
            
            while s[R] in curr:
                curr.remove(s[L])
                L += 1
            curr.add(s[R])
            length = max(length, len(curr))

        return length

        