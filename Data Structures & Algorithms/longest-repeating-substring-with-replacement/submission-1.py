class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        
        for letter in range(ord('A'), ord('Z') + 1):
            replace = 0
            L = 0

            for R in range(len(s)):
                if ord(s[R]) != letter:
                    replace += 1
                while replace > k:
                    if ord(s[L]) != letter:
                        replace -= 1
                    L += 1

                length = max(length, R - L + 1)
                
        return length
                


                

        