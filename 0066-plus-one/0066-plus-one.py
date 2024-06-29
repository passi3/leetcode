class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        for i, element in enumerate(digits):
            total = total*10 + element
        total_plus_one = total + 1
        new_list = [int(j) for j in str(total_plus_one)]
        return new_list