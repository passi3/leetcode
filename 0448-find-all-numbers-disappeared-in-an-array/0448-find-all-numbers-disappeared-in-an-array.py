class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        items=set(range(1,len(nums)+1))
        return list(items-set(nums))