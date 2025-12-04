class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        cnt = 0
        
        while start != 0 or goal !=0:
            print(start, goal)
            if start%2 != goal%2:
                cnt += 1
            start //= 2
            goal //= 2
        return cnt