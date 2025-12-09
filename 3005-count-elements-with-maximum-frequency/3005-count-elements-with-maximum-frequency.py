class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cntMap = dict()
        maxFreq = 0
        for num in nums:
            currFreq = nums.count(num)
            cntMap[num] = cntMap.get(0, currFreq)
            if currFreq > maxFreq:
                maxFreq = currFreq
        
        return sum([v for k, v in cntMap.items() if v == maxFreq])