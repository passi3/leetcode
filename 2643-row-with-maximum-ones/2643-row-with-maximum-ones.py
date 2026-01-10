class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        hashmap = {}
        for i, row in enumerate(mat):
            hashmap[i] = hashmap.get(i, row.count(1))

        maxCnt = max(hashmap.values())
        return [min([k for k, v in hashmap.items() if v == maxCnt]), maxCnt]