class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        
        for k in counter:
            copy = counter.copy()
            copy[k] -= 1

            if copy[k] == 0:
                del copy[k]
                
            if len(set(copy.values())) == 1:
                return True
        
        return False