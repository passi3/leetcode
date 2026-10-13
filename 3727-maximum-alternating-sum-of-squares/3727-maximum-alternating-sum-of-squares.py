class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        squares = sorted([num * num for num in nums])
        
        return sum(squares[n//2:]) - sum(squares[:n//2])