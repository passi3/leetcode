class Solution:
    def reverseByType(self, s: str) -> str:
        res = []
        letters = []
        others = []
        
        for i in s:
            if i.isalpha():
                letters.append(i)
            else:
                others.append(i)

        for i in s:
            if i.isalpha():
                res += letters.pop()
            else:
                res += others.pop()
        return "".join(res)