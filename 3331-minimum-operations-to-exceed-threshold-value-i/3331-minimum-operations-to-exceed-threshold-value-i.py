class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = 0

        while nums[0] <= k:
            if nums[0] == k:
                break
            else:
                nums = nums[1:]
                cnt += 1

        return cnt