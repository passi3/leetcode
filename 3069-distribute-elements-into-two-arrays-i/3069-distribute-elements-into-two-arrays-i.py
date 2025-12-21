class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        prefix, suffix = [nums[0]], [nums[1]]
        for i in range(2, len(nums)):
            if prefix[-1] > suffix[-1]:
                prefix.append(nums[i])
            else:
                suffix.append(nums[i])

        return prefix + suffix