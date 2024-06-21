class Solution:
    def romanToInt(self, s: str) -> int:
        romanSymbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        string_length = len(s)

        for i in range(string_length):
            this_value = romanSymbols[s[i]]

            if i+1 < string_length and this_value < romanSymbols[s[i+1]]:
                total -= this_value
            else:
                total += this_value
        return total
