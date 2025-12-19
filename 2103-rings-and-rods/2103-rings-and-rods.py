class Solution:
    def countPoints(self, rings: str) -> int:
        cnt = 0
        length = len(rings) // 2
        if length < 3:
            return cnt

        rods = {}
        for i in range(length):
            color = rings[2*i]
            rod = int(rings[2*i + 1])
            print(color, rod)
            rods[rod] = rods.get(rod, [0, 0, 0])
            if color == "R":
                rods[rod][0] +=1
            elif color == "G":
                rods[rod][1] +=1
            else:
                rods[rod][2] +=1
            print(rods)
        
        for k, v in rods.items():
            if not v.__contains__(0):
                cnt += 1
        return cnt