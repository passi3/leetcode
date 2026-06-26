class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount % 10 >= 5:
            p = (purchaseAmount // 10 + 1) * 10
        else:
            p = (purchaseAmount // 10) * 10
        
        return 100 - p