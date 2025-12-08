class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        commandDict = {"UP": -n, "DOWN": n, "LEFT": -1, "RIGHT": 1}
        res = 0
        for command in commands:
            res += commandDict[command]
        
        return res