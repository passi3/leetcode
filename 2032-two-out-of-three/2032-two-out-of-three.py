class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        hash = {}
        numsAll = [nums1, nums2, nums3]

        for nums in numsAll:
            for num in set(nums):
                hash[num] = hash.get(num, 0) + 1

        return [k for k, v in hash.items() if v >= 2]