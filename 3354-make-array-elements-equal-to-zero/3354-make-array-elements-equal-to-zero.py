class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 2
        cnt = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                continue
            lSum, rSum = sum(nums[:i]), sum(nums[i+1:])
            diff = abs(lSum - rSum)
            if diff == 0:
                cnt += 2
            elif diff == 1:
                cnt += 1

        return cnt