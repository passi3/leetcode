class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l = [[1]]   # 반환 리스트의 초깃값 세팅
        for i in range(rowIndex):    # 입력값에 대한 l의 각 리스트에 대한 순회
            r = [1]
            for j in range(1, i+1):   # 리스트 내 원소 채우기
                r.append(l[i][j-1] + l[i][j])
            r.append(1)
            l.append(r)
        return l[-1]