class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        res = -1
        target = float('inf')

        for i, v in enumerate(capacity):
            if v >= itemSize and v < target:
                target = v
                res = i
        
        return res