class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        digits = []

        for ch in s:
            if ch.isdigit():
                digits.append(ch)
            else:
                letters.append(ch)
        
        lengthLetters = len(letters)
        lengthDigits = len(digits)
        
        if abs(lengthLetters - lengthDigits) > 1:
            return ""
        
        elif lengthLetters > lengthDigits:
            return "".join([letters[i]+digits[i] for i in range(lengthDigits)] + [letters[-1]])
        elif lengthLetters < lengthDigits:
            return "".join([digits[i]+letters[i] for i in range(lengthLetters)] + [digits[-1]])
        else:
            return "".join([digits[i]+letters[i] for i in range(lengthLetters)])