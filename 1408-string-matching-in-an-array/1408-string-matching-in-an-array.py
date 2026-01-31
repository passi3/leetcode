class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for word in words:
            if len([target for target in words if word in target]) > 1:
                res.append(word)
        return res