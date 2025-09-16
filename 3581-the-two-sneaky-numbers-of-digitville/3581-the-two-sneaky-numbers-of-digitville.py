class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        once = []
        res = []
        for num in nums:
            if num not in once:
                once.append(num)
            else:
                res.append(num)
        
        return res