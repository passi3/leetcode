class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        prev = False
        for letter in command:
            if letter == "(":
                prev = True
            elif prev and letter == ")":
                prev = False
                res += "o"
            elif letter not in [")"]:
                prev = False
                res += letter
        return res