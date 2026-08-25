class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        counter = Counter(s)

        for v in counter.values():
            if v % 2 == 0:
                res += v
            else:
                res += v-1
        
        return res if res == len(s) else res + 1