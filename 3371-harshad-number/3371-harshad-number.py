class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        def recur_divide(y: int) -> int:
            if y < 10:
                return y
            return y % 10 + recur_divide(y//10)

        harshad = recur_divide(x)
        return harshad if x % harshad == 0 else -1