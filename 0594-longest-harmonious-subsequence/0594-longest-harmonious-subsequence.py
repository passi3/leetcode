class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        maxLen = 0

        for num in cnt:
            if num +1 in cnt:
                maxLen = max(maxLen, cnt[num] + cnt[num+1])
        
        return maxLen