class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        cnt = 0
        words.sort()
        for i in range(len(words)-1):
            if words[i][::-1] in words[i+1:]:
                print(words[i])
                cnt += 1
        
        return cnt