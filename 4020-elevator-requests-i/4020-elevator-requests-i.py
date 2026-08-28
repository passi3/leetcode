class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        take = 0
        curr = 0
        for r in requests:
            take += abs(curr-r)
            curr = r
        return take