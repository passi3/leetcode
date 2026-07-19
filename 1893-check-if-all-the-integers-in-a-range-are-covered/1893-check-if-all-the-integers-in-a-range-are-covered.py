class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right+1):
            for r in ranges:
                if i in range(r[0], r[1]+1):
                    break
            else:
                return False
            
        return True