class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in range(len(operations)):
            op = operations[i]
            if op == "C":
                res.pop()
            elif op == "D":
                res.append(int(res[-1])*2)
            elif op == "+":
                res.append(int(res[-1]) + int(res[-2]))
            else:
                res.append(int(op))

        print(res)
        
        return sum(res)