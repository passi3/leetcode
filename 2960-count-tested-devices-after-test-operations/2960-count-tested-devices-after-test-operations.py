class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        cnt = 0

        for b in batteryPercentages:
            if b > cnt:
                cnt += 1
        return cnt