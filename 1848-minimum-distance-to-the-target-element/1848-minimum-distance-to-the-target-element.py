class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        indices = defaultdict(list)

        for i, num in enumerate(nums):
            indices[num].append(i)
        
        return min([abs(start-i) for i in indices[target]])
