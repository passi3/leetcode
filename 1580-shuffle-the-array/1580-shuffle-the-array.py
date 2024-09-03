class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        for i in range(int(len(nums)/2)):
            output.append(nums[i])
            output.append(nums[i+int(len(nums)/2)])

        return output