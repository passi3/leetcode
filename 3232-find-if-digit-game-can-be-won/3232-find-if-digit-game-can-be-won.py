class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        double = 0
        single = 0
        for num in nums:
            if num // 10 != 0:
                double += num
            else:
                single += num
        
        return double != single