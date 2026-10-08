class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k %= len(mat[0])

        for row in mat:
            if row != row[k:] + row[:k]:
                return False
            
        return True
