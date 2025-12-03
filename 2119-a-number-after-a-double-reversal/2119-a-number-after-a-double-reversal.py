class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        numStr = str(num)

        return len(numStr) == len(str(int(numStr[::-1])))