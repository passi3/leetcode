class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        res = []
        for i, word in enumerate(words):

            if word[0] not in set("aeiouAEIOU"):
                word = word[1:] + word[0]
            word += "ma"
            word += "a"*(i+1)
            res.append(word)

        return " ".join(res)