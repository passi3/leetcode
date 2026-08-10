class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        cnt = 0
        while nums != sorted(nums):
            adjSum = float("inf")
            idx = -1
            for i in range(len(nums)-1):
                target = nums[i] + nums[i+1]
                if target < adjSum:
                    adjSum = target
                    idx = i
            nums = nums[:idx] + [adjSum] + nums[idx+2:]
            cnt += 1

        return cnt