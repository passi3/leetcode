class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split()
        prev = 0

        for word in s:
            try: 
                curr = int(word)
                if curr > prev:
                    prev = curr
                else:
                    return False
            except:
                continue

        return True