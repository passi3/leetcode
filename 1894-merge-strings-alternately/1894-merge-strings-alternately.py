class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        for i in range(max(len(word1),len(word2))):
            try:
                result+=word1[i]
            except:
                pass
            try:
                result+=word2[i]
            except:
                pass
        return result