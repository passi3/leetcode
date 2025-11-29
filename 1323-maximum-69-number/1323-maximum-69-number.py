class Solution:
    def maximum69Number (self, num: int) -> int:
        m = num
        strNum = list(str(num))
        for i in range(len(strNum)):
            chgNum = strNum.copy()
            print(chgNum)
            if int(chgNum[i]) == 6:
                chgNum[i] = '9'
            else:
                chgNum[i] = '6'
            
            new = int(''.join(chgNum))
            if new > m:
                m = new 
        
        return m
