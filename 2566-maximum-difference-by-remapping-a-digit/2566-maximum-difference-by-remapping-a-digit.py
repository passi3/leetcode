class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        max_s = s
        for ch in s:
            if ch != "9":
                max_s = s.replace(ch, "9")
                break

        min_s = s.replace(s[0], "0")

        return int(max_s) - int(min_s)