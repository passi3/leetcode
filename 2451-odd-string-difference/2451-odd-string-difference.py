class Solution:
    def oddString(self, words: List[str]) -> str:
        diff_counter = {}

        for w in words:
            key = tuple(ord(w[i+1]) - ord(w[i]) for i in range(len(w)-1))
            
            if key not in diff_counter:
                diff_counter[key] = [w]
            else:
                diff_counter[key].append(w)
        
        for k, v in diff_counter.items():
            if len(v) == 1:
                return v[0]
            