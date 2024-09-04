class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        prev = 0
        for account in accounts:
            now = sum(account)
            prev = max(prev, now)
        return prev