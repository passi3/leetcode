class Solution:
    def countLargestGroup(self, n: int) -> int:
        dp = [0] * (n+1)
        count = [0] * 60

        for i in range(1, n+1):
            dp[i] = dp[i//10] + i%10
            count[dp[i]] += 1
        
        maxSize = 0
        for i in range(len(count)):
            if maxSize < count[i]:
                maxSize = count[i]
        return len([cnt for cnt in count if cnt == maxSize])