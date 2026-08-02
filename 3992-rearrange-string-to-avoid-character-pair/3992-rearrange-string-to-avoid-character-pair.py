class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        counter = Counter(s)
        return y*counter[y] + "".join([k*v for k, v in counter.items() if k != x and k != y]) + x*counter[x]