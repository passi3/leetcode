class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        prefix, suffix = p.split("*")
        idx = s.find(prefix)
        if idx == -1:
            return False
        return s.find(suffix, idx+len(prefix)) != -1