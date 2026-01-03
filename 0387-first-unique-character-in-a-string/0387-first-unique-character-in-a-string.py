class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = defaultdict(list)
        for i in range(len(s)):
            h[s[i]].append(i)
        
        for k, v in h.items():
            if len(v) == 1:
                return v[0]
        return -1