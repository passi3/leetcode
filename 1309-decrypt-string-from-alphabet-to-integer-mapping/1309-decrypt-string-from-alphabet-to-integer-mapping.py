class Solution:
    def freqAlphabets(self, s: str) -> str:
        nums = []
        pivot = 0

        while pivot < len(s):
            if pivot + 2 <len(s) and s[pivot+2] == "#":
                num = int(s[pivot:pivot+2])
                nums.append(chr(num + 96))
                pivot += 3
            else:
                num = int(s[pivot])
                nums.append(chr(num + 96))
                pivot += 1
        
        return "".join(nums)