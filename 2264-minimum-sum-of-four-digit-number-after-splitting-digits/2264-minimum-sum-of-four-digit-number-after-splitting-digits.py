class Solution:
    def minimumSum(self, num: int) -> int:
        nums = []
        for char in str(num):
            nums.append(int(char))

        nums.sort()
        return sum(nums[:2])*10 + sum(nums[2:])