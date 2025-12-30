class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        setNums = set(nums)
        listNums = list(setNums)
        cnt = 0

        for num in listNums:
            if num != 0:
                cnt += 1
        
        return cnt