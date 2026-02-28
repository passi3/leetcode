class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for operation in operations:
            if operation.startswith("-") or operation.endswith("-"):
                res -= 1
            else:
                res += 1
        
        return res