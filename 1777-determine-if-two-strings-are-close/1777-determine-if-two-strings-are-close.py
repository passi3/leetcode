class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        elif set(word1) != set(word2):
            return False
        
        result1, result2 = list(), list()
        for char in set(word1):
            result1.append(word1.count(char))
            result2.append(word2.count(char))

        result1.sort()
        result2.sort()
        if result1 == result2:
            return True
        else:
            return False