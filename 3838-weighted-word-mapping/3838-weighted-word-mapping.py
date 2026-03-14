class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ""
        d = dict()
        reverse = list(chr(i) for i in range(122, 96, -1))
        for i in range(26):
            d[chr(i+97)] = weights[i]

        for word in words:
            sub = 0
            for char in word:
                sub += d[char]
            res += reverse[sub % 26]

        
        return res