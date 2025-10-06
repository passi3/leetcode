class Solution:
    def sortSentence(self, s: str) -> str:
        split_s = s.split()
        res = [""]*len(split_s)
        for item in split_s:
            res[int(item[-1])-1] = item[:-1]
        return " ".join(res)