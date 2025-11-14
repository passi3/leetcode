class Solution:
    def hasSameDigits(self, s: str) -> bool:
        length = len(s)

        while length > 2:
            digitSum = ""
            for i in range(length-1):
                digitSum += str((int(s[i]) + int(s[i+1]))%10)

            s = digitSum
            length -= 1
        
        return int(s) % 10 == int(s) // 10