class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        valDict = dict()
        res = []
        for num in set(nums):
            cnt = nums.count(num)
            if cnt not in valDict.keys():
                valDict[cnt] = [num]
            else:
                valDict[cnt] += [num]
            valDict[cnt].sort()
        
        for cnt in sorted(valDict):
            res += [num for num in valDict[cnt][::-1] for _ in range(cnt)]

        return res