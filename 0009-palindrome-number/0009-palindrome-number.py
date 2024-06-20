class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        string_invese = string[-1::-1]
        if string == string_invese:
            return True
        else:
            return False