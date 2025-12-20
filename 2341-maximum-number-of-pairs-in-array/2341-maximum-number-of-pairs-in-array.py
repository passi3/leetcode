class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        hash = {}
        firstCnt, secondCnt = 0, 0
        for num in set(nums):
            hash[num] = hash.get(num, nums.count(num))
            firstCnt += hash[num] // 2
            secondCnt += hash[num] % 2
        
        return [firstCnt, secondCnt]