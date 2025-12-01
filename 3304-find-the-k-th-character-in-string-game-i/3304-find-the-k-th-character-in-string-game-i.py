class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        while len(word) <= k:
            appendWord = ''.join(chr(ord(char)+1) for char in word)
            word+= appendWord

        return word[k-1]