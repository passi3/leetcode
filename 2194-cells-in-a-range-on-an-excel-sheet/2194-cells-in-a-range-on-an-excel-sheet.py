class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        colStart = s[0]
        rowStart = s[1]
        colEnd = s[3]
        rowEnd = s[4]

        return [f"{chr(col)}{row}" for col in range(ord(colStart), ord(colEnd)+1) for row in range(int(rowStart), int(rowEnd)+1)]