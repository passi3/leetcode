class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)

        for i in range(l):
            n = l - i

            if nums[i] >= n and (i == 0 or nums[i - 1] < n):
                return n
                
        return -1