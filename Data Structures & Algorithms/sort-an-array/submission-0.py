class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left, right):
            unified = []
            l = 0
            r = 0
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    unified.append(left[l])
                    l += 1
                else:
                    unified.append(right[r])
                    r += 1
            if l < len(left):
                unified.extend(left[l:])
            if r < len(right):
                unified.extend(right[r:])

            return unified

        def mergeSort(L, R):
            if L == R:
                return [nums[L]]
            
            M = (L+R)//2
            left = mergeSort(L, M)
            right = mergeSort(M+1, R)
            return merge(left, right)
        
        return mergeSort(0, len(nums)-1)
            

