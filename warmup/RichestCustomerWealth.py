class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_ = -1
        for account in accounts:
            sum_ = sum(account)
            if sum_ > max_:
                max_ = sum_
        return max_