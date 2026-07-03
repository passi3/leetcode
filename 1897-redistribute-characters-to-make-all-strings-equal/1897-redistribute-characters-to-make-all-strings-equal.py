class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        l = len(words)
        counter = Counter("".join(words))
        
        return all(v % l == 0 for v in counter.values())