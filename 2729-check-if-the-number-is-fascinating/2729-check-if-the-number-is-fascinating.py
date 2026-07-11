class Solution:
    def isFascinating(self, n: int) -> bool:
        def listToNums(n: int) -> [str]:
            return list(str(n))

        nums = listToNums(n) + listToNums(n*2) + listToNums(n*3)

        return len(nums) == len(set(nums)) and "0" not in nums and len(nums) == 9