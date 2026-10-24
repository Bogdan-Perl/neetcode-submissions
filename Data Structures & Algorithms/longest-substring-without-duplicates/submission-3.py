class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        L = 0
        length = float("-inf")

        for R in range(len(s)):
            
            while s[R] in curr:
                curr.remove(s[L])
                L += 1
            curr.add(s[R])
            length = max(length, len(curr))

                    
            
        return length if length != float('-inf') else 0


        