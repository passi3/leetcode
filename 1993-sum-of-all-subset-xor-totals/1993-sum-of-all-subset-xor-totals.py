class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def ssum(sub, idx):
            if idx == len(nums):
                return sub
            return ssum(sub, idx+1) + ssum(sub^nums[idx], idx+1)
        return ssum(0,0)