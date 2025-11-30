class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            digitSum = 0
            while num > 0:
                digitSum += num % 10
                num //= 10
            res.append(digitSum)
            print(res)
        return min(res)