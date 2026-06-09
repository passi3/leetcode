class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        res = [0] * 26

        d = dict()
        for i, char in enumerate(s):
            if char not in d:
                d[char] = [i]
            else:
                d[char].append(i)

        for char in d.keys():
            values = d[char]
            if len(values) >= 2:
                target = d[char][-1] - d[char][0] - 1
                
                if target != distance[ord(char) - 97]:
                    return False
        
        return True
