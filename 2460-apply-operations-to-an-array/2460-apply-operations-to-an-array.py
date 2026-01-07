class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            elif i == len(nums)-1:
                res.append(nums[i])
            elif nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
                res.append(nums[i])
            else:
                res.append(nums[i])
        return res + [0]*nums.count(0)