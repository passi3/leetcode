class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = [letter.lower() for letter in s if letter.isalnum()]
        
        return filtered_s == filtered_s[::-1]