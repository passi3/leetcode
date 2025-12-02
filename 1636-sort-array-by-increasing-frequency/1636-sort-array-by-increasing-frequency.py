class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dic = {}
        res = []

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        for item in sorted(dic.items(), key=lambda x: (x[1], -x[0])):
            res.extend([item[0]] * item[1])
        
        return res