class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = 0
        a = 0

        for num in nums:
            a |= num
        
        def dfs(i, curr):
            nonlocal res

            if i == len(nums):
                if curr == a:
                    res += 1
                return
            dfs(i+1, curr | nums[i])
            dfs(i+1, curr)
        
        dfs(0, 0)

        return res