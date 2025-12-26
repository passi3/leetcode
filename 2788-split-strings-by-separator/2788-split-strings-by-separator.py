class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        
        for word in words:
            res += [string for string in word.split(separator) if string != ""]
        
        return res