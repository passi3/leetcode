class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0

        for i in range(len(nums)):
            cnt = 0
            num = nums[i]

            while i > 0:
                q, r = i//2, i%2
                if r == 1:
                    cnt += 1

                if cnt > k:
                    break
                i = q
            
            if cnt == k:
                res += num
        
        return res