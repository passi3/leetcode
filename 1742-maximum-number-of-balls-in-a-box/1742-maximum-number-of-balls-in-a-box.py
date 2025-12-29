class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        hash = dict()

        for ball in range(lowLimit, highLimit+1):
            digitSum = 0
            while ball > 0:
                digitSum += ball%10
                ball //= 10
            hash[digitSum] = hash.get(digitSum, 0) + 1
        
        return max([v for v in hash.values()])