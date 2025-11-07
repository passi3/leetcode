class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        res = sum(tasks[0])
        for task in tasks[1:]:
            taskTime = sum(task)
            if taskTime < res:
                res = taskTime
        return res