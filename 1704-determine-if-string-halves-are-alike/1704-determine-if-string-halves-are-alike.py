class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        cnt = 0
        l = int(len(s)/2)
        for char in s[:l]:
            if char in vowels:
                cnt += 1

        for char in s[l:]:
            if char in vowels:
                cnt -= 1
                if cnt < 0:
                    return False
        
        if cnt == 0:
            return True
        else:
            return False