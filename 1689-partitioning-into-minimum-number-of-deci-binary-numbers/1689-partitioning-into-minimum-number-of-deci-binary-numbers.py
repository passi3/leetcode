class Solution:
    def minPartitions(self, n: str) -> int:
        for char in "9876543210":
            if char in n:
                return int(char)