class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        l = len(code)
        res = [0] * l
        if k == 0:
            return res

        for i in range(l):
            if k > 0:
                if i+1+k > l:
                    res[i] = sum(code[i+1:] + code[:(i+1+k)%l])
                else:
                    res[i] = sum(code[i+1:i+1+k])
            else:
                if i+k < 0:
                    res[i] = sum(code[:i] + code[(i+k)%l:])
                else:
                    res[i] = sum(code[i+k:i])
        
        return res