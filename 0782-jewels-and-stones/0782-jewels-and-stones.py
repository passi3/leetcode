class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        for i in jewels:
            for j in stones:
                if i == j:
                    result += 1
        return result