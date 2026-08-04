class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in nums:
            reflection = int(bin(i)[2:][::-1], 2)
            res.append((reflection, i))
        
        res.sort()
        
        return [x[1] for x in res]