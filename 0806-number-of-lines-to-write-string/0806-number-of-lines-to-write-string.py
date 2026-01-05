class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        res = [0] * 2

        hash = dict()
        for i, width in enumerate(widths):
            hash[chr(i+97)] = hash.get(chr(i+97), width)

        stackWidth = 0
        stackS = []
        for char in s:
            if stackWidth+hash[char] <= 100:
                stackWidth += hash[char]
                stackS.append(char)
                continue
            else:
                res[0] += 1
                stackS = [char]
                stackWidth = hash[char]
        res[0] += 1
        res[1] = stackWidth
        return res