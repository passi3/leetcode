class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = 0

        for char in s:
            charIdx = ord(char)-96
            while charIdx > 0:
                res += charIdx%10
                charIdx = charIdx//10
        
        k -= 1

        while k > 0:
            temp = 0
            while res > 0:
                temp += res % 10
                res //= 10
            res = temp
            k -= 1

        return res