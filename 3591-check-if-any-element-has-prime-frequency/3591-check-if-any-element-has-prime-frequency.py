class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for v in counter.values():
            if self.isPrime(v):
                return True
        return False

    def isPrime(self, n: int) -> bool:
        if n < 2:
            return False
        
        for i in range(2, int(n ** 0.5) + 1):
            if n % i ==0:
                return False
        return True
