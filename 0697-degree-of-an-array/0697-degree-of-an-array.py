class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        indices = defaultdict(list)

        for i in range(len(nums)):
            indices[nums[i]].append(i)
        
        degree = max([len(v) for v in indices.values()])
        
        return min([max(v) - min(v) + 1 for v in indices.values() if len(v) == degree])