class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        res = -1

        for i, num in enumerate(nums):
            if num != i:
                res = num if res == -1 else (res & num)
        
        return 0 if res == -1 else res