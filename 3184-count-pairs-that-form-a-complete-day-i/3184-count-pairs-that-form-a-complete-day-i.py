class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hash = {}
        cnt = 0

        for hour in hours:
            check = (24 - hour) % 24
            if check in hash:
                cnt += hash[check]
            if hour % 24 in hash:
                hash[hour % 24] += 1
            else:
                hash[hour % 24] = 1

        return cnt