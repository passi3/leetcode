class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [""] * len(s)
        for i, indice in enumerate(indices):
            res[indice] = s[i]

        return "".join(res)
