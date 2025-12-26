class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hash = {}

        for i in arr:
            hash[i] = hash.get(i, 0) + 1
        
        res = [k for k, v in hash.items() if k == v]
        return max(res) if len(res) > 0 else -1