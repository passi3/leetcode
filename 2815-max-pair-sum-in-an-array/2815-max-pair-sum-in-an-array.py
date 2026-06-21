from collections import defaultdict

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = -1
        digits = defaultdict(list)

        for num in nums:
            max_digit = max(str(num))
            digits[max_digit].append(num)
        
        for v in digits.values():
            if len(v) == 1:
                continue
            v = sorted(v, reverse=True)
            res = max(res, sum(v[:2]))
        
        return res