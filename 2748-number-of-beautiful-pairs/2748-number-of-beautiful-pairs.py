class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        res = 0
        
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a
        
        n = len(nums)
        for i in range(n-1):
            a = nums[i]

            while a >= 10:
                a //= 10

            for j in range(i+1, n):
                b = nums[j] % 10

                if gcd(a, b) == 1:
                    res += 1
        
        return res