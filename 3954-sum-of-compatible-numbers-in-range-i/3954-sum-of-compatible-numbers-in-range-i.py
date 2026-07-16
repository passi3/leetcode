class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        compatibles = []

        for i in range(n+k+1):
            if abs(n-i) <= k and (n & i) == 0:
                compatibles.append(i)
        
        return sum(compatibles)