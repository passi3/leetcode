class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxLen = 0
        for sentence in sentences:
            lenSentence = len(sentence.split())
            if lenSentence > maxLen:
                maxLen = lenSentence
        return maxLen