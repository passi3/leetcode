class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        l = 0
        r = len(s)-1
        
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                left = s[:l] + s[l+1:]
                right = s[:r] + s[r+1:]
                
                if left == left[::-1] or right == right[::-1]:
                    return True
                
                return False