class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        pivot = float("inf")
        res = pivot
        l = len(nums)

        for j in range(1, l-1):
            left, right = pivot, pivot
            
            for i in range(j):
                if nums[i] < nums[j] and nums[i] < left:
                    left = nums[i]
            
            for k in range(j+1, l):
                if nums[k] < nums[j] and nums[k] < right:
                    right = nums[k]
            
            if left != pivot and right != pivot:
                res = min(res, left + nums[j] + right)
                
        return res if res != pivot else -1