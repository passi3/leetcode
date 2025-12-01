class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)-1):
            curr, nxt = nums[i], nums[i+1]
            print(curr, nxt)
            if curr >= nxt:
                diff = curr - nxt
                nums[i+1] += diff + 1
                cnt += diff+1
                continue
                
        return cnt