class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        output = 0
        for i in range(len(operations)):
            if "+" in operations[i]:
                output += 1
            elif "-" in operations[i]:
                output -= 1
        
        return output