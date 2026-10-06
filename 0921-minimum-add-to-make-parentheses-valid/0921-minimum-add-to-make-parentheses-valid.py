class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        invalid = 0
        valid = 0

        for c in s:
            if c == "(":
                invalid += 1
            else:
                if invalid > 0:
                    invalid -= 1
                else:
                    valid += 1
            
        return valid + invalid