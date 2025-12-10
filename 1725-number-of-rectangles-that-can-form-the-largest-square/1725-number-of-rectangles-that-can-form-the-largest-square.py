class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        cnt = 0
        maxLen = max([min(l, w) for l, w in rectangles])
        
        for rectangle in rectangles:
            if maxLen == min(rectangle):
                cnt += 1

        return cnt
