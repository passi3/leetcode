class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n == 2:
            return True
        
        dx = coordinates[1][0] - coordinates[0][0]
        dy = coordinates[1][1] - coordinates[0][1]

        for i in range(1, n-1):
            if (coordinates[i+1][0] - coordinates[i][0]) * dy != (coordinates[i+1][1] - coordinates[i][1]) * dx:
                return False
        
        return True
