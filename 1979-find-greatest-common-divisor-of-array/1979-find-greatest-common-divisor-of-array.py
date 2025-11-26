class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)

        while largest % smallest != 0:
            smallest, largest = largest % smallest, smallest

        return smallest