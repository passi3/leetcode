class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        listt=list(s)
        listt.sort(reverse=True)
        listt.append(listt.pop(0))
        return "".join(listt)