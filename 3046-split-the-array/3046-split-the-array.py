class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        nums.sort()
        l = len(nums)//2
        num1 = []
        num2 = []
        
        for num in nums:
            if num not in num1:
                num1.append(num)
                nums.remove(num)
        
        if len(num1) == l and len(nums) == l:
            for i in range(len(nums)-1):
                if nums[i+1] == nums[i]:
                    return False
            return True
        else:
            return False
            