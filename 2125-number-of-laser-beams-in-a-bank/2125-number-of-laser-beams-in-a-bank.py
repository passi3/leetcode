class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        curr = bank[0].count("1")
        for floor in bank[1:]:
            cnt = floor.count("1")
            if cnt != 0:
                print(curr, cnt)
                res += curr * cnt
                curr = cnt
        
        return res