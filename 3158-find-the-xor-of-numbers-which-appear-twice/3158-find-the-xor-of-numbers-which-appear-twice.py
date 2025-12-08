class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        cntDict = dict()
        res = 0
        
        for num in nums:
            cntDict[num] = cntDict.get(num, 0) + 1

        for k, v in cntDict.items():
            if v == 2:
                res ^= k

        return res
            