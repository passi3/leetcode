class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        res = -1
        n = len(nums)
        nums.sort()

        for i in range(n):
            for j in range(i, n):
                if nums[j] > 2 * nums[i]:
                    break
                    
                res = max(nums[i] ^ nums[j], res)

        return res