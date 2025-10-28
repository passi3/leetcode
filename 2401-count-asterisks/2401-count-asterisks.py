class Solution:
    def countAsterisks(self, s: str) -> int:
        res = 0
        prefix = True
        split_s = s.split('|')
        for p in split_s:
            if prefix == False:
                prefix = True
                pass
            else:
                res += p.count('*')
                prefix = False
        return res