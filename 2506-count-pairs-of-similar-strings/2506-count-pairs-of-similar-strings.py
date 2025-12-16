from collections import defaultdict

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        cnt = defaultdict(int)

        for word in words:
            key = frozenset(word)
            cnt[key] += 1
        
        res = 0
        for v in cnt.values():
            res += v * (v-1) // 2

        return res