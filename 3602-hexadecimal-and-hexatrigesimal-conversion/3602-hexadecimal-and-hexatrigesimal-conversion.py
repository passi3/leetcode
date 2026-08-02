class Solution:
    def concatHex36(self, n: int) -> str:
        vals = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        d, t = n**2, n**3
        hex16, hex36 = "", ""
        
        while d > 0:
            q, r = d//16, d%16
            hex16 = vals[r] + hex16
            d = q
        
        while t > 0:
            q, r = t//36, t%36
            hex36 = vals[r] + hex36
            t = q
        
        return hex16 + hex36