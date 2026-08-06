class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]

        prefixSum = 0
        
        for num in nums:
            prefixSum += num
            self.prefix.append(prefixSum)
            
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)