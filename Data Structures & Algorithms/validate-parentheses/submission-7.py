class Solution:
    def isValid(self, s: str) -> bool:
        p = { 
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }

        opening = []
        k = 0
        
        for char in s:
            if char in p:
                opening.append(char)
            elif opening and char == p[opening[-1]]:
                opening.pop()
            else:
                return False
                
        return len(opening) == 0

