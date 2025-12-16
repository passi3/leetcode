class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt=0
        freq1 = Counter(words1)
        freq2 = Counter(words2)
        
        for word in words1:
            if freq1[word] == 1 and freq2[word] == 1:
                cnt+=1
        return cnt