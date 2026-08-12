class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = []
        curr = 0
        for num in pref:
            res.append(num^curr)
            curr = num
        
        return res