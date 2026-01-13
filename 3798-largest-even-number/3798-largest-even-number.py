class Solution:
    def largestEven(self, s: str) -> str:
        charSet = set(s.rstrip())
        if "2" not in charSet:
            return ""
        elif "1" not in charSet:
            return s
        
        res = []
        for char in s.rstrip()[::-1]:
            if len(res) == 0 and char == "1":
                continue
            res = [char]+res
        return "".join(res)