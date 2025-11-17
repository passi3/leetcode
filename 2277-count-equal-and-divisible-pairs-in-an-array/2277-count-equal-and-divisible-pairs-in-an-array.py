class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        l = len(nums)
        res = 0
        for i in range(l-1):
            for j in range(i+1, l):
                if (nums[i] == nums[j]) and (i*j) % k == 0:
                    res += 1
        return res