class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n <= 2:
            return nums

        right_max = [0] * n
        right_max[-1] = nums[-1]
        
        for i in range(n-2, -1, -1):
            right_max[i] = max(nums[i], right_max[i+1])

        res = [nums[0]]
        left_max = nums[0]
        
        for i in range(1, n-1):
            if nums[i] > left_max or nums[i] > right_max[i+1]:
                res.append(nums[i])
            left_max = max(left_max, nums[i])
        
        res.append(nums[-1])
        return res