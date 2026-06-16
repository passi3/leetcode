class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        can_eat = int(len(candyType) / 2)
        set_candy = len(set(candyType))

        if set_candy <= can_eat:
            return set_candy
        else:
            return can_eat