class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        start = points[0]
        time = 0
        for point in points[1:]:
            time += max(abs(start[0] - point[0]), abs(start[1] - point[1]))
            start = point
        return time
