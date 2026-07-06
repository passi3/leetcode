class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        max_digit = 0
        range_map = defaultdict(list)

        for num in nums:
            str_num = str(num)
            l, s = int(max(str_num)), int(min(str_num))
            range_map[l-s].append(num)
            max_digit = max(max_digit, l-s)
        
        return sum(range_map[max_digit])