class Solution:
    def countOdds(self, low: int, high: int) -> int:
        pivot = high - low + 1
        
        if pivot % 2 == 0:
            return pivot // 2
        
        if low % 2 == 0:
            return pivot // 2
        else:
            return pivot // 2 + 1