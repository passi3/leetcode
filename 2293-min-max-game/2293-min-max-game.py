class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        while n != 1:
            newNums = []
            for i in range(n//2):
                if i % 2 == 0:
                    newNums.append(min(nums[2*i: 2*i+2]))
                elif i % 2 == 1:
                    newNums.append(max(nums[2*i: 2*i+2]))
            nums = newNums
            n = n//2
        return nums[0]