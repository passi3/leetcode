class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res = 0

        for f in fruits:
            placed = False

            for i, b in enumerate(baskets):
                if b >= f:
                    baskets[i] = 0
                    placed = True
                    break
            
            if not placed:
                res += 1
            
        return res