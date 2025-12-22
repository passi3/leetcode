class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        longest = -1
        hash = {}
        for i in range(len(s)):
            if s[i] not in hash:
                hash[s[i]] = [i]
            else:
                hash[s[i]].append(i)
        
        for indices in hash.values():
            length = max(indices) - min(indices) - 1
            if length > longest:
                longest = length
        return longest