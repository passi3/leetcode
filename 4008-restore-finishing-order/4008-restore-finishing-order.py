class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        res = list()
        for i in order:
            if i in friends:
                res.append(i)
        
        return res