class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        res = float('inf')

        idx = nums.index(0)
        is_increasing = True
        is_decreasing = True

        for i in range(n):
            curr = nums[(idx+i) % n]
            if curr != i:
                is_increasing = False
            if curr != (n-i) % n:
                is_decreasing = False
        
        if not is_increasing and not is_decreasing:
            return -1
        
        if is_increasing:
            res = min(res, idx)
            res = min(res, 2 + n - idx)
        
        if is_decreasing:
            res = min(res, n - idx)
            res = min(res, 2 + idx)

        return res