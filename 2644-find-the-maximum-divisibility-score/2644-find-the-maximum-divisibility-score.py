class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        score = 0
        res = float("inf")
        
        for d in divisors:
            count = sum([True for n in nums if n % d == 0])
            if count > score:
                score = count
                res = d
            elif count == score:
                res = min(res, d)
        
        return res