class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        numsSum = sum(nums)
        while numsSum >=0 and numsSum % k != 0:
            print(numsSum)
            numsSum -= 1
            cnt+=1
        return cnt