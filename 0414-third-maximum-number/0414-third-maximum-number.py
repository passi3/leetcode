class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sort = [float("-inf")] * 3
        seen = set()

        for num in nums:
            if num in seen:
                continue
            elif num < sort[2]:
                pass
            elif num < sort[1]:
                sort[2] = num
            elif num < sort[0]:
                sort[2] = sort[1]
                sort[1] = num
            elif num > sort[0]:
                sort = [num, sort[0], sort[1]]
            seen.add(num)
        
        if sort[-1] == float("-inf"):
            return sort[0]
        
        return sort[-1]