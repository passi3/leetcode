class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0

        for word in words:
            counter = Counter(word)
            for k, v in counter.items():
                if chars.count(k) < v:
                    break
            else:
                res += len(word)
        
        return res