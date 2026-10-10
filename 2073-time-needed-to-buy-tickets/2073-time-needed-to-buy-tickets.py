class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        return sum(min(t , tickets[k] if i <= k else tickets[k] -1) for i, t in enumerate(tickets))