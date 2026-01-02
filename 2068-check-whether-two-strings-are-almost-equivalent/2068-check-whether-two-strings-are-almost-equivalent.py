class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        charSet = set(word1).union(set(word2))
        
        for char in charSet:
            if abs(word1.count(char) - word2.count(char)) >3:
                return False
        
        return True