class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = 0
        for word in words:
            for char in word:
                if char not in allowed:
                    break
            else:
                cnt+=1
        return cnt