class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        hash = {}
        items = items1+items2
        for item in items:
            v, w = item
            hash[v] = hash.get(v, 0) + w
        
        return [[k, v] for k, v in sorted(hash.items())]