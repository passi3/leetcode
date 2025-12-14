class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        vals = []
        for string in strs:
            try:
                vals.append(int(string))
            except:
                vals.append(len(string))
        
        return max(vals)