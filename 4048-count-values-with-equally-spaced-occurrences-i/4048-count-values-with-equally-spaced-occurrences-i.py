class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        res = 0
        indices = defaultdict(list)
        
        for i, num in enumerate(nums):
            indices[num].append(i)
        
        for j in indices.keys():
            if len(indices[j]) == 3:
                if indices[j][1] - indices[j][0] == indices[j][2] - indices[j][1]:
                    res += 1

        return res