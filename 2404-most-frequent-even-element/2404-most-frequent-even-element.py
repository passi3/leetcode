class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counter = Counter([n for n in nums if n % 2 == 0])
        
        if not counter:
            return -1
        
        res, cnt = -1, -1
        
        for k, v in counter.items():
            if v > cnt or (v == cnt and k < res):
                res, cnt = k, v
        
        return res