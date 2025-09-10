class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        cnt = 0
        for num1 in nums1:
            for num2 in nums2:
                cnt += (num1 % (num2 * k) == 0)
        
        return cnt