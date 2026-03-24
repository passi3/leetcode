class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cnt_ = 0
        cntL = 0
        cntR = 0
        for char in moves:
            if char == "L":
                cntL += 1
            elif char == "R":
                cntR += 1
            else:
                cnt_ += 1
        
        return abs(cntL - cntR) + cnt_