class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        common = [x for x in nums1 if x in set(nums2)]
        if common:
            return min(common)
        nums = [min(nums1), min(nums2)]
        nums = sorted(set(nums))
        return int("".join(map(str, nums)))