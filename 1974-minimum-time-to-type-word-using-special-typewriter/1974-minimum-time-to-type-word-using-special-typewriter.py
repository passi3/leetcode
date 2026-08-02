class Solution:
    def minTimeToType(self, word: str) -> int:
        ptr = 0
        cnt = 0

        for char in word:
            target = ord(char)-ord('a')
            diff = abs(target - ptr)
            
            cnt += min(diff, 26 - diff)
            cnt += 1

            ptr = target
        
        return cnt
                