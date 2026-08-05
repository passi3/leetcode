class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        l = len(s)
        for i in range(0, l, 2*k):
            if i + k <= l:
                target = s[i: i+k]
                s[i: i+k] = target[::-1]
            else:
                target = s[i:]
                s[i:] = target[::-1]
        
        return "".join(s)