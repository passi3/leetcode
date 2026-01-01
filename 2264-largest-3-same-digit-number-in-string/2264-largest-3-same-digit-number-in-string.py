class Solution:
    def largestGoodInteger(self, num: str) -> str:
        substr = []
        cnt = 1
        prev = num[0]
        for char in num[1:]:
            if char == prev:
                cnt += 1
            else:
                prev = char
                cnt = 1
            
            if cnt == 3:
                substr.append(int(char))
            
        return str(max(substr)) * 3 if len(substr) > 0 else ""