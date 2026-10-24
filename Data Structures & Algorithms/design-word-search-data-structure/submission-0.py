class TrieNode:
    def __init__(self):
        self.children = {}
        self.w = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.w = True
        
    def search(self, word: str) -> bool:
        def dfs(curr, j):
            if j == len(word):
                return curr.w
            if word[j] == '.':
                for child in curr.children.values():
                    if dfs(child, j+1): return True
                return False
            else:
                if word[j] not in curr.children:
                    return False
                return dfs(curr.children[word[j]], j+1)
        return dfs(self.root, 0)
