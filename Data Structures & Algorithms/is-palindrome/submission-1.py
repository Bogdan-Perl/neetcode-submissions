class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.casefold()

        l = 0
        r = len(st) - 1
        while l < r:
            if not self.alphanumeric(st[l]):
                l += 1
                continue
            if not self.alphanumeric(st[r]):
                r -= 1
                continue
                
            if (st[l] != st[r]):
                return False
            l += 1
            r -= 1
        return True
            
    def alphanumeric(self, c):
        return (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))
        

        