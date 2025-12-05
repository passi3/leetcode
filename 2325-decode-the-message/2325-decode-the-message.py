class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        res = ""
        keyMap = dict()
        i = 97
        for char in key:
            keyMap[' '] = 32
            if char not in keyMap:
                keyMap[char] = i
                i += 1

        print(keyMap)
        for j in range(len(message)):
            res += chr(keyMap[message[j]])
        return res 