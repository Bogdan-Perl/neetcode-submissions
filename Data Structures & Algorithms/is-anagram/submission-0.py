class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictT = {char:0 for char in set(t)}
        dictS = {char:0 for char in set(s)}

        for charactor in t:
            dictT[charactor] += 1
        for charactor in s:
            dictS[charactor] += 1
        
        return dictS == dictT