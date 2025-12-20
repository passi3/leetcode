class Solution:
    def sortString(self, s: str) -> str:
        res = []
        hash = {}
        for char in s:
            hash[char] = hash.get(char, 0) + 1
        
        keys = sorted(hash.keys())
        asc = True
        
        while len(res) < len(s):
            if asc:
                for key in keys:
                    if hash[key] > 0:
                        hash[key] -= 1
                        res.append(key)
            else:
                for key in keys[::-1]:
                    if hash[key] > 0:
                        hash[key] -= 1
                        res.append(key)
            
            asc = not asc
        
        return "".join(res)