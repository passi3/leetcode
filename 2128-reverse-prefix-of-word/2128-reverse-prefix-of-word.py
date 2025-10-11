class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        occIndex = word.index(ch)
        return word[:occIndex+1][::-1] + word[occIndex+1:]