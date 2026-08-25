class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        target = ""

        for i in range(len(bits)):
            if i == len(bits)-1 and target == "":
                return True
            target += str(bits[i])
            if target in ["0", "10", "11"]:
                target = ""
        return False