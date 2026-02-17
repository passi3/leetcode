class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        res = []
        slowest = 0
        prev = 0
        for i, curr in enumerate(releaseTimes):
            if curr - prev > slowest:
                slowest = curr - prev
                res = [keysPressed[i]]
            elif curr - prev == slowest:
                res.append(keysPressed[i])
            prev = curr
        return max(res)