class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        result = []
        for num in nums:
            if num == 0:
                cnt += 1
            else:
                result.append(num)
        
        for i in range(1, cnt+1):
            result.append(0)
        nums[:] = result