class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        numDict = dict()
        nums = nums1 + nums2
        for num in nums:
            if num[0] not in numDict:
                numDict[num[0]] = num[1]
            else:
                numDict[num[0]] += num[1]
        
        return sorted(numDict.items(), key=lambda x: x[0], reverse=0)