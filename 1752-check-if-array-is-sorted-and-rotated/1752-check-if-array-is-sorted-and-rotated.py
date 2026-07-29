class Solution:
    def check(self, nums: List[int]) -> bool:
        copied = sorted(nums)

        for x in range(len(nums)):
            for i in range(len(nums)):
                if not nums[(i+x) % len(nums)] == copied[i]:
                    break
            else:
                return True
        return False