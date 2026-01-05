class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def checkBoardColor(x: str, y: str) -> bool:
            # return 1 if coordinates's color is black, else white.
            if ord(x) % 2 == 1:
                if int(y) % 2 == 1:
                    isBlack = True
                else:
                    isBlack = False
            else:
                if int(y) % 2 == 0:
                    isBlack = True
                else:
                    isBlack = False
            return isBlack
            
        x1, y1 = coordinate1.strip()
        x2, y2 = coordinate2.strip()
        return checkBoardColor(x1, y1) == checkBoardColor(x2, y2)
        