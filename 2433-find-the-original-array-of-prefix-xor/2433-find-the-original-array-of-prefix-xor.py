class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref) == 1:
            return pref
        
        res = [pref[0]]
        for i in range(1, len(pref)):
            res.append(pref[i-1]^pref[i])
        
        return res