class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xPoints = sorted(set([point[0] for point in points]))

        if len(xPoints) == 1:
            return 0

        prev = abs(xPoints[0] - xPoints[1])
        
        for i in range(1, len(xPoints)):
            curr = abs(xPoints[i-1] - xPoints[i])
            if curr > prev:
                prev = curr

        return prev

