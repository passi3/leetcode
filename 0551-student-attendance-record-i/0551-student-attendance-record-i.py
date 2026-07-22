class Solution:
    def checkRecord(self, s: str) -> bool:
        As = 0
        Ls = 0
        
        for c in s:

            if c == "L":
                Ls += 1

                if Ls == 3:
                    return False
            else:
                Ls = 0
                if c == "A":
                    As += 1

                    if As == 2:
                        return False
        
        return True