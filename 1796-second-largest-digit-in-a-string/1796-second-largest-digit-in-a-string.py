class Solution:
    def secondHighest(self, s: str) -> int:
        largest, secondary = -1, -1
        for c in s:
            if c.isdigit():
                target = int(c)
                if target > largest:
                    secondary = largest
                    largest = target
                elif largest > target > secondary:
                    secondary = target
        
        return secondary