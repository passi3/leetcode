class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        cnt = 0
        length = len(colors)

        for i in range(length):
            first = colors[i]
            second = colors[(i+1)%length]
            third = colors[(i+2)%length]

            if first != second and second != third:
                cnt += 1
        
        return cnt