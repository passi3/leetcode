class Solution:
    def dayOfYear(self, date: str) -> int:
        months = [0, 31, 59 ,90, 120, 151, 181, 212, 243, 273, 304, 334]
        year, month, day = map(int, date.split("-"))
        
        res = months[month-1] + day

        if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) and month > 2:
            res += 1
        
        return res