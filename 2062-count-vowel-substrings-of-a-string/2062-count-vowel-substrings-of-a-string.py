class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        cnt = 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for vowel in vowels:
            if vowel not in word:
                return cnt

        for i in range(len(word)-4):
            for j in range(i+5, len(word)+1):
                if set(word[i:j]) == vowels:
                    cnt += 1
        
        return cnt