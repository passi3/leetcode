class Solution:
    def isHappy(self, n: int) -> bool:
        prevs = [n]
        while n != 1:
            n = sum([int(char)**2 for char in str(n)])
            if n not in prevs:
                prevs.append(n)
            else:
                return False
        return True