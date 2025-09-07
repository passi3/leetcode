class Solution:
    def removeStars(self, s: str) -> str:
        result = []
        for letter in s:
            if letter != "*":
                result.append(letter)
            else:
                result.pop()
        return "".join(result)