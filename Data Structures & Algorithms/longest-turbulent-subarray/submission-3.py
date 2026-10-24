class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        wasBigger = False #True
        wasSmaller = False
        # False and False is consective dups, restart count
        # True and False means next must be smaller, else restart count
        # False and True means next must be bigger, else restart count
        maxCount = 0 #2
        count = 0

        if not len(arr)-1:
            return 1
        
        for x in range(1, len(arr)):
            isBigger = False
            isSmaller = False
            if arr[x] > arr[x-1]:
                isBigger = True
                if wasSmaller:
                    count+=1
                else:
                    count=1
                wasSmaller = False
                wasBigger = True
            elif arr[x] < arr[x-1]:
                isSmaller = True
                if wasBigger:
                    count+=1
                    wasBigger = False
                else:
                    count=1
                wasSmaller = True
                wasBigger = False
            else:
                count = 0
                wasSmaller = False
                wasBigger = False
            
            maxCount = max(maxCount, count)
            
        return maxCount +1
            
            


