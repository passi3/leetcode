class Solution:
    def countKeyChanges(self, s: str) -> int:
        sList = list(s)

        for i in range(len(sList)):
            sList[i] = sList[i].lower()

        cnt = 0
        for i in range(len(sList)-1):
            if sList[i] != sList[i+1]:
                cnt += 1

        return cnt