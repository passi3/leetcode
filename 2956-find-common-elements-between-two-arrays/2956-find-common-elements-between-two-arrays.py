class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:

        def cntIndicesInNums(nums1: List[int], nums2: List[int]) -> int:
            cnt = 0
            nums2 = set(nums2)
            for num in nums1:
                if num in nums2:
                    cnt += 1
            
            return cnt

        return [cntIndicesInNums(nums1, nums2), cntIndicesInNums(nums2, nums1)]
        