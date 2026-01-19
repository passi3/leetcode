class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            digitProduct = 1
            m = n
            while m > 0:
                digitProduct *= m % 10
                m //= 10
            if digitProduct % t == 0:
                return n
            else:
                n += 1