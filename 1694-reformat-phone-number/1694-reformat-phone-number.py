class Solution:
    def reformatNumber(self, number: str) -> str:
        nums = number.replace(" ", "").replace("-", "")
        res = []
        l = len(nums)
        
        while l > 0:
            if l > 4:
                res.append(nums[:3])
                nums = nums[3:]
                l -= 3
            elif l == 4:
                res.append(nums[:2])
                nums = nums[2:]
                res.append(nums)
                l -= 4
            else:
                res.append(nums)
                l = 0
        
        return "-".join(res)