class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res = 0
        l = len(nums)

        for i in range(l // 2):
            res += int(str(nums[i]) + str(nums[-i-1]))

        if l % 2 != 0:
            res += nums[l // 2]
        
        return res