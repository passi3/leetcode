class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        setS = set(sentence)
        return len(setS) == 26