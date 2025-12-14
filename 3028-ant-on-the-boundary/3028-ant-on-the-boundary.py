class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        cnt = 0
        pos = 0
        for num in nums:
            pos += num
            if pos == 0:
                cnt += 1
        
        return cnt