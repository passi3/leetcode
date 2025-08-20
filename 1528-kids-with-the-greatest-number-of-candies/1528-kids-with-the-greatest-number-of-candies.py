class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = candies[0]
        for candy in candies:
            if candy > greatest:
                greatest = candy
        result = []
        for i,candy in enumerate(candies):
            candy += extraCandies
            result.append(candy >= greatest)
        return result