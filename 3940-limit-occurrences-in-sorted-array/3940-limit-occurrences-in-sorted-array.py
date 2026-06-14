class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        res = [nums[0]]
        target = res[0]
        cnt = 1

        for num in nums[1:]:
            if num != target:
                target = num
                cnt = 1
            elif num == target and cnt < k:
                cnt += 1
            else:
                continue
            res.append(num)
        
        return res