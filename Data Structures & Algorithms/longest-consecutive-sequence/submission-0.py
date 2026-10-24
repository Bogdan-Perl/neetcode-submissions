class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #key=tar, val=sequence.len
        x = set(nums)
        longest = 0

        for num in nums:
            length = 1
            if num-1 not in x:
                while num+length in x:
                    length += 1
                longest = max(longest, length)
        return longest
            