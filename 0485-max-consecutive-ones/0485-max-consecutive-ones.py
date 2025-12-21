class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCnt = 0
        cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
                maxCnt = max(cnt, maxCnt)
            else:
                cnt = 0
        
        return maxCnt