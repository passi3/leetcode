class Solution:
    def splitNum(self, num: int) -> int:
        num = sorted(map(int, str(num)))
        num1, num2 = [], []

        for i, v in enumerate(num):
            if i % 2 == 0:
                num1.append(str(v))
            else:
                num2.append(str(v))
        
        return int("".join(num1)) + int("".join(num2))