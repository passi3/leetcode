class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        firstNum = ''.join([f'{ord(char)-97}' for char in firstWord])
        secondNum = ''.join([f'{ord(char)-97}' for char in secondWord])
        targetNum = ''.join([f'{ord(char)-97}' for char in targetWord])
        return int(firstNum) + int(secondNum) == int(targetNum)