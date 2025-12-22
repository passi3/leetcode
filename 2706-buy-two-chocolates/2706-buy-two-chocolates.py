class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices = [price for price in prices if price < money]
        length = len(prices)
        
        if length <= 1:
            return money

        prices.sort()
        if sum(prices[:2]) > money:
            return money
        return money - sum(prices[:2])