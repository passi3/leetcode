class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0
        for log in logs:
            if log.endswith("../"):
                cnt = max(cnt-1, 0)
            elif log.endswith("./"):
                continue
            else:
                cnt += 1
        return cnt