class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        hash = {'0':0,'1':0}
        cnt = 0
        l = 0
        
        for r in range(len(s)):
            hash[s[r]] = 1 + hash.get(s[r], 0)
            while hash['0'] > k and hash['1'] > k :
                hash[s[l]] = hash.get(s[l],0) - 1
                l+=1
            cnt += r - l + 1

        return cnt