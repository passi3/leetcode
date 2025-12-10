class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        nums = list(num)
        for i in range(len(nums)):
            if nums[-1] == "0":
                nums.pop()
        
        return "".join(nums)