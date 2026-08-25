class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        num = ""

        for n in nums:
            num += str(n)
            if int(num, 2) % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        
        return res