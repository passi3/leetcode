class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        res = 0
        cnt = defaultdict(int)
        n = len(nums)

        for b in range(n-3, 0, -1):
            for d in range(b+2, n):
                cnt[nums[d] - nums[b+1]] += 1

            for a in range(b):
                res += cnt[nums[a] + nums[b]]
        
        return res