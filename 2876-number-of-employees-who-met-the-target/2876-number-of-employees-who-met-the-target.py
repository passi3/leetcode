class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        initial = 0
        for element in hours:
            if element >= target:
                initial += 1
        return initial