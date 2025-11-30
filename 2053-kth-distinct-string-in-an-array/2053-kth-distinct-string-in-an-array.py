class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = dict()
        for char in arr:
            cnt = 0
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
            
        distinct = [k for k in arr if freq[k] == 1]

        return distinct[k-1] if k <= len(distinct) else ""