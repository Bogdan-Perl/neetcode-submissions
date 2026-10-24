class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grouped = dict()

        for word in strs:
            sortedWordList = sorted(word)
            sortedWord = ''.join(char for char in sortedWordList)

            if sortedWord in grouped:
                grouped[sortedWord].append(word)
            else:
                grouped[sortedWord] = [word]


        return grouped.values()
        

        
        