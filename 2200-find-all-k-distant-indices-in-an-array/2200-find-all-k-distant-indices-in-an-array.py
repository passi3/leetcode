class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        n = len(nums)
        key_indices = [i for i, x in enumerate(nums) if x == key]
        
        last_added = -1
        
        for j in key_indices:
            start = max(last_added + 1, j - k)
            end = min(n - 1, j + k)
            
            for i in range(start, end + 1):
                res.append(i)
                last_added = i
                
        return res