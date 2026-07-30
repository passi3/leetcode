class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def invertSec(str) -> str:
            hh = int(str[:2])
            mm = int(str[-2:])
            return hh*(60**2) + mm*60
        start = max(invertSec(event1[0]), invertSec(event2[0]))
        end = min(invertSec(event1[1]), invertSec(event2[1]))
        
        return start <= end