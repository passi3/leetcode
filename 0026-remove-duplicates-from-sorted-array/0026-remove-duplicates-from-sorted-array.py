class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        insert_position = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[insert_position]:
                insert_position += 1
                nums[insert_position] = nums[i]
        
        return insert_position + 1