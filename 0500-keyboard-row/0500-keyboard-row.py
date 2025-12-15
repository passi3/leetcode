class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        res = []
        for i in range(len(words)):
            word = set(words[i].lower())
            for row in rows:
                if set(row).intersection(word) == word:
                    res.append(words[i])
        
        return res