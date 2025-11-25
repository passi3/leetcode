class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avgs = []
        for i in range(len(nums)//2):
            nums.sort()
            smallest, largest = nums[0], nums[-1]
            nums = nums[1:-1]
            avgs.append((smallest+largest)/2)
        return min(avgs)