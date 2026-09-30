class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        res = 0
        def to_minutes(time_str: str) -> int:
            h, m = map(int, time_str.split(':'))
            return h * 60 + m
        
        diff = to_minutes(correct) - to_minutes(current)

        for unit in [60, 15, 5, 1]:
            res += diff//unit
            diff %= unit
        
        return res