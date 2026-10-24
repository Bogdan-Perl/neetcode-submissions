class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        words = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                tot = ord(char) - ord('a')
                count[tot] += 1
            key = tuple(count)   
            words[key].append(word)
        
        return words.values()

