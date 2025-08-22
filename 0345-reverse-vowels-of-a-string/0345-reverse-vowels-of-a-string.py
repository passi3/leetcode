class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        reverse = []
        result = ""
        for i, letter in enumerate(s):
            if letter in vowels:
                reverse.append(letter)
            else:
                pass

        for i, letter in enumerate(s):
            if letter in vowels:
                result += reverse.pop()
            else:
                result += letter
        return result

        return s
        