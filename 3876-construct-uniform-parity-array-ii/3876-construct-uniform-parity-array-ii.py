class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        target = min((num for num in nums1 if num%2 == 1), default=None)

        if target is None:
            return True
        
        for num in nums1:
            if num % 2 == 0 and num < target:
                return False

        return True