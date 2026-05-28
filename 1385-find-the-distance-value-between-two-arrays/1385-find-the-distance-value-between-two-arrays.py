class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0

        for v1 in arr1:
            if all(abs(v1 - v2) > d for v2 in arr2):
                res += 1

        return res