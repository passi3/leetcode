class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        keys = set(list(counter1.keys())+list(counter2.keys()))
        for key in keys:
            cnt = min(counter1[key], counter2[key])
            res += [key]*cnt
        return res