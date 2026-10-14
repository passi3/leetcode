class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num or sum == 0:
            return ""
        nums = []

        for _ in range(num):
            d = min(9, sum)
            nums.append(str(d))
            sum -= d
        
        return "".join(nums)